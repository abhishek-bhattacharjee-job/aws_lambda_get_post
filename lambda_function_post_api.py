import json

def lambda_handler(event, context):
    req_data = json.loads(event["body"])
    var1 = req_data["var1"]
    var2 = req_data["var2"]
    response_headers = {
        'Content-Type': 'application/json'
    }
    return {
        'statusCode': 200,
        'headers': response_headers,
        'body': json.dumps({ "var1" : var1, "var2" : var2 })
    }
