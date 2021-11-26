import boto3
import os

import boto3

region = 'us-east-2'
instances = ['i-0600b5889ba3288c1',]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handlerstart(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))

def lambda_handlerstop(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
       for printout in pythonins['Instances']:
           if(printout['InstanceId']=='i-0600b5889ba3288c1'):
                print(printout['InstanceId'])
                print(printout['InstanceType'])
                if(printout['State']['Name']=='stopped'):
                    lambda_handlerstart("1","2")
                else:
                    lambda_handlerstop("1","2")

           


