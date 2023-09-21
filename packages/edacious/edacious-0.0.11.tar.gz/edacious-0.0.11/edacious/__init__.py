import asyncio
import uvicorn
import threading
from time import sleep
from quickbelog import Log
from fastapi import FastAPI
from datetime import datetime
from inspect import getfullargspec
from abc import ABC, abstractmethod

EVENT_TYPE_KEY = 'event-type'
EVENT_ID_KEY = 'event-id'

app = FastAPI(title='Event Listener')

EVENT_TYPE_HANDLERS = {}
EVENT_COUNT = 0
LISTENER_SW_ID = 'No ID'


class EventListener(ABC):

    def __init__(self, *args, **kwargs):
        self._event_count = 0
        self._seconds_to_wait = kwargs.get('seconds_to_wait', 5)
        self._run_switch = True

    def get_event_count(self) -> int:
        return self._event_count

    def set_seconds_to_wait(self, seconds: float):
        self._seconds_to_wait = seconds

    def stop(self):
        self._run_switch = False

    @abstractmethod
    def fetch(self) -> list:
        pass

    @abstractmethod
    def event_handling_error(self, event: dict):
        pass

    @abstractmethod
    def event_handling_done(self, event: dict):
        pass

    async def process_event(self, event_type: str, event: dict):
        event_processing(event_type=event_type, event=event)
        self.event_handling_done(event=event)
        self._event_count += 1
        global EVENT_COUNT
        EVENT_COUNT += 1

    async def process_all_events(self, events: list):
        for event in events:
            if EVENT_TYPE_KEY in event:
                event_type = event[EVENT_TYPE_KEY]
                try:
                    asyncio.create_task(self.process_event(event_type=event_type, event=event))
                except NotImplementedError as ex:
                    Log.debug(str(ex))
                except Exception as ex:
                    Log.exception(f'Processing event type {event_type} failed with {ex}')
                    self.event_handling_error(event=event)
            else:
                Log.warning(f'Event does not have event-type attribute {event}')

    def run(self, run_api: bool = False, api_port: int = 8888):
        def infinity_loop():
            global LISTENER_SW_ID
            LISTENER_SW_ID = Log.start_stopwatch(msg='Starting event listener')
            while self._run_switch:
                asyncio.run(self.process_all_events(events=self.fetch()))
                sleep(1)
        if run_api:

            listener_thread = threading.Thread(target=infinity_loop, name="event-listener")
            listener_thread.start()
            uvicorn.run(app=app, host="0.0.0.0", port=api_port)
            listener_thread.join()
        else:
            infinity_loop()

    @staticmethod
    @app.get("/")
    @app.get("/health")
    def api_health_check():
        return {"time": datetime.utcnow(), "status": 'OK'}

    @staticmethod
    @app.get("/status")
    def api_status():
        return {
            "uptime": Log.stopwatch_seconds(stopwatch_id=LISTENER_SW_ID, print_it=False),
            "handlers": {k: [f.__qualname__ for f in funcs] for k, funcs in EVENT_TYPE_HANDLERS.items()},
            "event_count": EVENT_COUNT,
            "time": datetime.utcnow(),
            "status": 'OK'
        }


def register_handler(event_type: str, func):
    global EVENT_TYPE_HANDLERS

    if is_valid_event_handler(func=func):
        if event_type in EVENT_TYPE_HANDLERS:
            EVENT_TYPE_HANDLERS.get(event_type).append(func)
        else:
            EVENT_TYPE_HANDLERS[event_type] = [func]
        Log.info(f'Handler {func.__qualname__} will be triggered for event type {event_type}.')


def is_valid_event_handler(func) -> bool:
    args_spec = getfullargspec(func=func)
    try:
        args_spec.annotations.pop('return')
    except KeyError:
        pass
    arg_types = args_spec.annotations.values()
    if len(arg_types) == 1 and issubclass(list(arg_types)[0], dict):
        return True
    else:
        raise TypeError(
            f'Function {func.__qualname__} needs one argument, type dict. Instead got the following spec: {args_spec}'
        )


def event_handler(event_type: str):
    def inner_func(func):
        register_handler(event_type=event_type, func=func)
        return func

    return inner_func


def event_processing(event_type: str, event: dict):
    handlers = EVENT_TYPE_HANDLERS.get(event_type, [])
    if len(handlers) == 0:
        raise NotImplementedError(f'Event type {event_type} does not have any implementation.')
    for e_handler in handlers:
        e_handler(event)
