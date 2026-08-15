from client import CloudAgentClusterContainerCoordinatorClient

def main():
    client = CloudAgentClusterContainerCoordinatorClient()
    res = client.coordinate_cluster({"task": "Distributed web research crawl", "model": "gpt-5.6"}, 16)
    print(f"Cluster ID: {res['allocated_cluster_id']}")
    print(f"Active Workers: {res['active_workers_count']}")
    print(f"Status: {res['dispatch_status']}")

if __name__ == "__main__":
    main()
