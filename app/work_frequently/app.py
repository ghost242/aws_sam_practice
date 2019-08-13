import os
from datetime import datetime

import boto3


def lambda_handler(event, context):
    q_url = os.environ.get('DATAPIPE_QUEUEURL')
    q_message = datetime.now().isoformat()
    q_client = boto3.client('sqs')
    q_client.send_message(
        QueueUrl=q_url,
        MessageBody=q_message
    )
    return {
        "statusCode": 200,
        "body": "send_to::{}<-{}".format(q_url, q_message)
    }
