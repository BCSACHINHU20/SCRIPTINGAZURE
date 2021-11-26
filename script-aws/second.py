import boto3
#conn=boto3.client('ec2')
#ec2_conn=boto3.resource('ec2')
ec2 = boto3.resource('ec2', region_name="us-east-2")
snapshot = ec2.create_snapshot(VolumeId='vol-09dacc183c072f171', TagSpecifications=[
    {
                'ResourceType': 'snapshot',
                'Tags': [
                              {
                                 'Key': 'Name',
                                 'Value': 'b680020bcsachinvolumesnap-id2'
                              }
                         ]
            }
     ])
tag=snapshot.create_tags[
            {
                     'Key': 'Name',
                     'Value': 'b680020bcsachinvolumesnap-id2'
            }]
print(snapshot)
"""
volume = ec2.create_volume(SnapshotId=snapshot.id, AvailabilityZone='us-west-2')
ec2.Instance('i-0600b5889ba3288c1').attach_volume(VolumeId=volume.id, Device='/dev/sdy')
#snapshot.delete()i 
"""      
~                                                                                                                                                                                                   
~                                                                                                                                                                                                   
~                                 