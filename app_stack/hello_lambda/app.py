import os

import boto3


def lambda_handler(event, context):
    try:
        bucket_name = os.environ.get('DATASTORE_BUCKETNAME')
        s3_client = boto3.client('s3')

        for record in event['Records']:
            print("test")
            payload = record["body"]
            print(str(payload))

            s3_client.meta.client.upload_fileobj(payload.encode('utf-8'),
                                                 bucket_name,
                                                 'test_file.txt')
    except Exception as e:
        code = 500
        msg = str(e)
    else:
        code = 200
        msg = 'Success'
    finally:
        return {
            'code': code,
            'message': msg
        }
