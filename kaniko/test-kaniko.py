from kubernetes import client, config
# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
def get_pods(podname):
    v1 = client.CoreV1Api()
    pod_list = v1.list_namespaced_pod(podname)
    for pod in pod_list.items:
        print(pod.metadata.name)

get_pods("next")