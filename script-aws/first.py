import boto3
conn=boto3.client('ec2')
response=conn.create_security_group(GroupName="b680020bcsachin-security-group",Description="created by sachin on 25 nov")
print("response of sec-group\n")
print(response)
conn.authorize_security_group_ingress(GroupId=response['GroupId'],IpProtocol='tcp',CidrIp='0.0.0.0/0',FromPort=22,ToPort=22)
keypair=conn.create_key_pair(KeyName="webkey")
print(keypair['KeyMaterial'])
#ami-020db2c14939a8efb
ec2_conn=boto3.resource('ec2')
instance=ec2_conn.create_instances(
    ImageId="ami-020db2c14939a8efb", MinCount=1,MaxCount=3,SecurityGroups=["b680020bcsachin-security-group"],KeyName="webkey",InstanceType="t2.macro")
print("\n instance is \n")
print(instance)
#  BlockDeviceMappings=[{"DeviceName": "/dev/xvda","Ebs" : { "VolumeSize" : 50 }}]
