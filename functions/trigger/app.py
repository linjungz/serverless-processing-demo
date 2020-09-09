import json
import boto3
from uuid import uuid4


# import requests


def lambda_handler(event, context):
    sfnclient = boto3.client('stepfunctions')
    count = 0

    for record in event['Records']:
        id=str(record["body"])
        print('Message Body: ', id)

        input_dict = {
            'id' : id
        }
        print(json.dumps(input_dict))

        response = sfnclient.start_execution(
            stateMachineArn = 'arn:aws-cn:states:cn-northwest-1:402202783068:stateMachine:VideoProcessStateMachine-oyOOuVQvTdLe',
            name = '{}-{}'.format(str(id), str(uuid4())),
            input = json.dumps(input_dict))

        print(response)
        
        count = count + 1
    
    print("Triggered Workflow: ", count)





    