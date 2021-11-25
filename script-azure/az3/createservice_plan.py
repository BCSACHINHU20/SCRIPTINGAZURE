import os

from azure.identity import AzureCliCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.resource import ResourceManagementClient
resource_client = ResourceManagementClient(
        credential=AzureCliCredential(),
        subscription_id="fcd4d0d9-59c4-451c-9665-a0001f80e9e2"
    )
web_client = WebSiteManagementClient(
        credential=AzureCliCredential(),
        subscription_id="fcd4d0d9-59c4-451c-9665-a0001f80e9e2"
    )
app_service_plan = web_client.app_service_plans.begin_create_or_update(
        "AZRG-USE2-CON-NPDHASHEDINAZUREINTERNALPOC-NPD-002",
        "b680020bcsachin-appserviceplan",
        {
          "name": "b680020bcsachin-appserviceplan",
          "type": "Microsoft.Web/serverfarms",
          "kind": "linux",
          "os": "linux",
          "location": "East US",
          "sku": {
            "name": "B1",
            "tier": "Basic",
            "size": "small",
            "family": "B",
            "capacity": "1"
          },
          "tags": {
          "name": "b680020bcsachin-appserviceplan"
    },
        }
    ).result()
print("Create app service plan:\n{}".format(app_service_plan))
