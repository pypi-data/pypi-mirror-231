import json
import boto3
import edacious
from quickbelog import Log

# Create SQS client
sqs = boto3.client('sqs')

MESSAGE_ATTRIBUTE_NAMES = 'MessageAttributeNames'
MESSAGE_ATTRIBUTES = 'MessageAttributes'
EVENT_BODY = 'Body'
EVENT_BODY_MESSAGE = 'Message'


class EventListener(edacious.EventListener):

    def __init__(self, sqs_url: str, visibility_timeout: int = 3, max_messages_to_fetch: int = 10):
        """
        :param sqs_url: AWS SQS url
        :param visibility_timeout: Visibility timeout when receiving messages is seconds
        :return:
        """

        self._sqs_url = sqs_url
        self._visibility_timeout = visibility_timeout
        self._max_messages_to_fetch = max_messages_to_fetch
        Log.info(f'Will listen to SQS {self._sqs_url}')
        super().__init__(tuple(), {})

    def fetch(self) -> list:
        response = sqs.receive_message(
            QueueUrl=self._sqs_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=self._max_messages_to_fetch,
            MessageAttributeNames=['All'],
            VisibilityTimeout=self._visibility_timeout,
            WaitTimeSeconds=0
        )

        if 'Messages' in response:
            events = []
            for msg in response['Messages']:

                try:
                    event = self.get_event_body(msg=msg)
                    event_type = self.get_event_type(msg=msg, event=event)
                    if event_type is not None:
                        event[edacious.EVENT_TYPE_KEY] = event_type
                    event['ReceiptHandle'] = msg['ReceiptHandle']
                    events.append(event)
                except json.JSONDecodeError:
                    Log.warning(f'Can not parse message body, ignoring this message. Got {msg.get("Body")}')
            return events
        else:
            return []

    @staticmethod
    def get_event_body(msg: dict) -> dict:
        even_body = msg.get(EVENT_BODY, {})
        if isinstance(even_body, str):
            even_body = json.loads(even_body)

        if EVENT_BODY_MESSAGE in even_body:
            even_body = even_body.get(EVENT_BODY_MESSAGE)

        if isinstance(even_body, str):
            even_body = json.loads(even_body)

        return even_body

    @staticmethod
    def get_event_type(msg: dict, event: dict) -> str:
        even_type = None
        if edacious.EVENT_TYPE_KEY in event:
            even_type = event.get(edacious.EVENT_TYPE_KEY)
        elif MESSAGE_ATTRIBUTES in msg:
            even_type = msg.get(
                        'MessageAttributes',
                        {}
                    ).get(edacious.EVENT_TYPE_KEY, {}).get('StringValue')
        else:
            msg_body = msg.get(EVENT_BODY, {})
            if isinstance(msg_body, str):
                msg_body = json.loads(msg_body)
            if MESSAGE_ATTRIBUTES in msg_body:
                even_type = msg_body.get('MessageAttributes', {}).get(edacious.EVENT_TYPE_KEY, {}).get('Value')
        return even_type

    def event_handling_error(self, event: dict):
        pass

    def event_handling_done(self, event: dict):
        # Delete received message from queue
        receipt_handle = event['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=self._sqs_url,
            ReceiptHandle=receipt_handle
        )
