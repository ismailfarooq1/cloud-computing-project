from kubernetes import client, config
from prometheus_api_client import PrometheusConnect

# Load Kubernetes configuration
config.load_kube_config()
v1 = client.CoreV1Api()

# Prometheus connection using FQDN
prom = PrometheusConnect(url="http://prometheus.default.svc.cluster.local:9090", disable_ssl=True)

def get_custom_metrics():
    # Example: Query Prometheus for CPU usage metric
    query = 'sum(rate(container_cpu_usage_seconds_total{container_name!="POD"}[5m])) by (pod)'
    result = prom.custom_query(query=query)
    
    # Parse and process metrics
    metrics = {}
    for sample in result:
        pod_name = sample['metric']['pod']
        cpu_usage = float(sample['value'][1])
        metrics[pod_name] = cpu_usage
    
    return metrics


def calculate_replicas(metrics):
    # Example logic to calculate replicas based on metrics
    if metrics['cpu_usage'] > 80:
        return 5  # Scale up to 5 replicas if CPU usage is high
    elif metrics['cpu_usage'] < 20:
        return 1  # Scale down to 1 replica if CPU usage is low
    else:
        return 3  # Default number of replicas

def scale_deployment():
    metrics = get_custom_metrics()
    replicas = calculate_replicas(metrics)
    
    # Update deployment
    body = {'spec': {'replicas': replicas}}
    v1.patch_namespaced_deployment_scale(name="ml-inference-deployment", namespace="default", body=body)

if __name__ == "__main__":
    scale_deployment()
