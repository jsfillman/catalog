from os import path

import yaml

from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "kaniko-test.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.CoreV1Api()
        resp = k8s_apps_v1.create_namespaced_pod(
            body=dep, namespace="next")
        print("Deployment created. status='%s'" % resp.metadata.name)


if __name__ == '__main__':
    main()