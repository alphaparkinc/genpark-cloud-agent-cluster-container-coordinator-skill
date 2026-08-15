class CloudAgentClusterContainerCoordinatorClient:
    def coordinate_cluster(self, agent_job_spec: dict, max_concurrency: int = 16) -> dict:
        return {
            "allocated_cluster_id": "cluster-worker-us-east-8021",
            "active_workers_count": 8,
            "dispatch_status": "AGENT_CLUSTER_ACTIVE_ROUTING"
        }
