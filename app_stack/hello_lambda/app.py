import json
import os

import boto3


def lambda_handler(event, context):
    try:
        print('Enter in LambdaHandler!!')
        bucket_name = os.environ.get('DATASTORE_BUCKETNAME')
        s3_client = boto3.client('s3')

        for record in event['Records']:
            print("test")
            payload = record["body"]
            print(str(payload), type(payload), repr(payload))

            s3_client.put()
            res = s3_client.upload_file(text,
                                        bucket_name,
                                        'test_file.txt')
            print(res)
    except Exception as e:
        code = 500
        msg = str(e)
        print("Error!! {}".format(msg))
    else:
        code = 200
        msg = 'Success'
        print("Success!! {}".format(msg))
    finally:
        return {
            "statusCode": code,
            "body": json.dumps({
                "message": msg
            }),
        }
