# list ecs services from the cluster using boto3
import boto3
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 list_ecs_services.py <cluster_name>")
        sys.exit(1)

    cluster_name = sys.argv[1]
    desired_count = sys.argv[2]

    client = boto3.client('ecs')
    response = client.list_services(cluster=cluster_name)
    
    # set scaling to desired count for each service
    for service in response['serviceArns']:
        print("Scaling a list of ecs services with desire count " + desired_count)
        print(service)
        client.update_service(cluster=cluster_name, service=service, desiredCount=int(desired_count))

if __name__ == "__main__":
    main()