import argparse
import os
import time
import googleapiclient.discovery

def create_instance(compute, project, zone, name, bucket):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-9').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    
    
    config = {
        'name': name,
        'machineType': machine_type
            
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END compute_apiary_create_instance]
compute = googleapiclient.discovery.build('compute', 'v1')
create_instance(compute, "us-gcp-ame-con-116-npd-1", "us-west2-a","b680020bcsachin-vm1" , "680020bcsachin-bucket")