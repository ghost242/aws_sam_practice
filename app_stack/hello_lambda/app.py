import json


def lambda_handler(event, context):
    for record in event['Records']:
       print ("test")
       payload=record["body"]
       print(str(payload))
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": {
                'context': context,
                'event': event
            }
            # "location": ip.text.replace("\n", "")
        }),
    }
