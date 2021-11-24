import googleapiclient.discovery
compute = googleapiclient.discovery.build('compute', 'v1')
def list_instances():
    result = compute.instances().list(project="us-gcp-ame-con-116-npd-1", zone="us-west2-a").execute()
    return result['items'] if 'items' in result else None
print(list_instances())