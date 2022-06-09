import boto3
import variable
from botocore import response

client = boto3.client('rds')
tagkey = variable.key
tagvalue = variable.value

def lambda_handler(event, context):

    arn = (event["detail"]["SourceArn"])

    instance_tags = client.list_tags_for_resource(ResourceName = arn)
    tag_list = instance_tags['TagList']
    tag = next(iter(filter(lambda tag: tag['Key'] == 'application-autoscaling:resourceId' and (tag['Value'] is not None and tag['Value'] != ''), tag_list)), None)
    if tag is None:
        print('This RDS is not Aurora Autoscaling Instance:',arn)
    else: 
      tag_key = tag['Key']
      if tag_key == 'application-autoscaling:resourceId':
        response = client.add_tags_to_resource(
        ResourceName = arn,
        Tags=[
            {
              'Key': tagkey,
              'Value': tagvalue
          },
        ]
        )
        print ('Add Tag RDS:',arn)
        print(response)