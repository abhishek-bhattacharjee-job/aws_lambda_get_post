import json

def lambda_handler(event, context):
    req_data = json.loads(event["body"])
    var1 = req_data["var1"]
    var2 = req_data["var2"]
    return {
        'statusCode': 200,
        'body': json.dumps({ "var1" : var1, "var2" : var2 })
    }
