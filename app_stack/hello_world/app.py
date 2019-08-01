import json
import os
import boto3

from urllib.parse import parse_qs


# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    q_name = ""
    try:
        q_name = os.environ.get('DATAPIPE_QUEUENAME')
        queries = parse_qs(event['body'])
        
        sqs_client = boto3.client('sqs')
        sqs_client.send_message(
            QueueUrl=q_name,
            MessageBody='hello')

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": q_name,
            }),
        }
    except Exception as e:
        return {
            "statusCode": 503,
            "body": json.dumps({
                "message": str(e) + q_name,
            }),
        }
