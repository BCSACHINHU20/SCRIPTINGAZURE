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
"""
print('\nStarting VM')
async_vm_start = compute_client.virtual_machines.begin_start(
"AZRG-USE2-CON-NPDHASHEDINAZUREINTERNALPOC-NPD-002", "b680020bcsachin-VM")
print(async_vm_start.result())
"""
print('\nDelete VM')
async_vm_delete = compute_client.virtual_machines.begin_delete(
"AZRG-USE2-CON-NPDHASHEDINAZUREINTERNALPOC-NPD-002", "b680020bcsachin-VM")
print(async_vm_delete.result())