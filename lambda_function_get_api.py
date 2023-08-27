import json

def lambda_handler(event, context):
    params = event["queryStringParameters"]
    return {
        'statusCode': 200,
        'body': json.dumps(params)
    }
