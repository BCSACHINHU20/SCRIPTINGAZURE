"""
rom azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
"""
"""
Subscription_Id =  "fcd4d0d9-59c4-451c-9665-a0001f80e9e2"
Tenant_Id = "36da45f1-dd2c-4d1f-af13-5abe46b99921"
Client_Id = "fcd4d0d9-59c4-451c-9665-a0001f80e9e2"
Secret = "xxxxx"

credential = ServicePrincipalCredentials(
        client_id=Client_Id,
        secret=Secret,
        tenant=Tenant_Id
        )

compute_client = ComputeManagementClient(credential, Subscription_Id)

vm_list = compute_client.virtual_machines.list_all()
# vm_list = compute_client.virtual_machines.list('resource_group_name')
i= 0
for vm in vm_list:
    array = vm.id.split("/")
    resource_group = array[4]
    vm_name = array[-1]
    statuses = compute_client.virtual_machines.instance_view(resource_group, vm_name).statuses
    status = len(statuses) >= 2 and statuses[1]

    if status and status.code == 'PowerState/running':
        print(vm_name)
"""
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
print('\nList VMs in subscription')
for vm in compute_client.virtual_machines.list_all():
    print("\tVM: {}".format(vm.name))
 # List VM in resource group
print('\nList VMs in resource group')
for vm in compute_client.virtual_machines.list("AZRG-USE2-CON-NPDHASHEDINAZUREINTERNALPOC-NPD-002"):
    print("\tVM: {}".format(vm.name))