import boto3 #Boto3 is the AWS SDK for Python


def lambda_handler(event, context):

    for i in event["Records"]:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["name"]
        object = i["s3"]["object"]["key"]

    client = boto3.client("ses")

    subject = 'Event = ' + str(action) + ' | Bucket = ' + bucket_name + ' | Object = ' + object
    body = """
        <br>
        The following files have been received from Source to Target 
        - {}
    """.format(object, ip)

    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}

    response = client.send_email(Source = "mayurmorwal@gmail.com", Destination = {"ToAddresses": ["mayur.morwal@adgear.com"]}, Message = message)

    return "Thanks"