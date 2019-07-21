import os

from kubernetes import client, config, watch
from kubernetes.config.config_exception import ConfigException

ns = os.environ.get('K8S_NAMESPACE', 'default')

try:
    # it works only if this script is run by K8s as a POD
    config.load_incluster_config()
except ConfigException:
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

v1 = client.CoreV1Api()


def list_pods():
    # Print POD list
    podList = v1.list_namespaced_pod(namespace=ns, watch=False)
    resourceVersion = podList.metadata.resource_version
    print("---- PodList ---")
    for pod in podList.items:
        print('pod name: {}'.format(pod.metadata.name))

    w = watch.Watch()
    for item in w.stream(v1.list_namespaced_pod,
        namespace=ns,
        watch=True,
        timeout_seconds=0
    ):
        pod = item['object']

        # parse POD events
        # new POD added
        if item['type'] == 'ADDED':
            print("Pod Added: {}".format(pod.metadata.name))

        # POD is removed
        if item['type'] == 'DELETED':
            print("pod deleted: {}".format(pod.metadata.name))


if __name__ == '__main__':
    list_pods()