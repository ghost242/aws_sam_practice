import json
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
    try:
        # q_url = os.environ.get('DATAPIPE_QUEUEURL')
        print(event['body'])
        # token=Xfpakwc2UcHmyfC18Aoj8bFq&team_id=TKLDUCN9Z&team_domain=paperplanghost242&channel_id=CKXRP1S2U&channel_name=general&user_id=UL00FGZ3Q&user_name=ohzakka&command=%2Fcmd&text=rule+test_job+add+%22++key+key+key.++%22+%3D+%22++++value.+value.++value.+++++%22&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FTKLDUCN9Z%2F707107124546%2FLuq4DO8ejsV5CJgkqXdWp1kk&trigger_id=718544137781.666470430339.b9d91783287813a4fa4073b85146891f

        queries = parse_qs(event['body'])
        print(queries)
        # {'token': ['Xfpakwc2UcHmyfC18Aoj8bFq'], 'team_id': ['TKLDUCN9Z'], 'team_domain': ['paperplanghost242'], 'channel_id': ['CKXRP1S2U'], 'channel_name': ['general'], 'user_id': ['UL00FGZ3Q'], 'user_name': ['ohzakka'], 'command': ['/cmd'], 'text': ['rule test_job add " key key key. " = " value. value. value. "'], 'response_url': ['https://hooks.slack.com/commands/TKLDUCN9Z/707107124546/Luq4DO8ejsV5CJgkqXdWp1kk'], 'trigger_id': ['718544137781.666470430339.b9d91783287813a4fa4073b85146891f']}
        # queries['text']
        # ['rule test_job add " key key key. " = " value. value. value. "']

        # sqs_client = boto3.client('sqs')
        # sqs_client.send_message(
        #     QueueUrl=q_url,
        #     MessageBody=queries['text'][0])
        #
        # client = WebClient(
        #     'xoxp-666470430339-680015577126-677406666020-6204ebbb70bbe4071c8abe7ebdacac45')
        # resp = client.chat_postMessage(
        #     channel=queries['channel_id'][0],
        #     text=queries['text'][0]
        # )
        # print(resp)

        code = 200
        message = 'Successfully received message!!'
    except Exception as e:
        code = 503
        message = 'Err::' + str(e)
    finally:
        return {
            "statusCode": code,
            "body": json.dumps({
                "message": message
            }),
        }
