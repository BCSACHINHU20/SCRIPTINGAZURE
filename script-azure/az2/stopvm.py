import os
import random
import string

from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

compute_client = ComputeManagementClient(
        credential=AzureCliCredential(),
        subscription_id="fcd4d0d9-59c4-451c-9665-a0001f80e9e2"
    )
print('\nStop VM')
async_vm_stop = compute_client.virtual_machines.begin_power_off(
"AZRG-USE2-CON-NPDHASHEDINAZUREINTERNALPOC-NPD-002", "b680020bcsachin-VM")
print(async_vm_stop.result())