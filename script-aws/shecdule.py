import boto3
import os
region = 'us-east-2'
instances = ['i-0600b5889ba3288c1',]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handlerstart(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
    os.environ['flagsofex']='stop'


def lambda_handlerstop(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    os.environ['flagsofex']='start'

if(os.getenv('flagsofex')=='start'):
    lambda_handlerstart("1","2")
else:
    lambda_handlerstop("1","2")

