# k8s-realtime-monitoring

## Services list

### __watcher__:  
TL;DR: Watcher calls the Kubernetes API from within the cluster to fetch the list of current pods across all namespaces  and publish it to RethinkDB.  

watcher's service account has a ClusterRoleBinding with `ClusterRole:view`.  
From within the pod, we take advantage of the auto-mounted service account's secrets to get a cert and token to call the `kubernetes.default` service.  
Watch period is 1 second


watcher first calls the Kubernetes API to get a current pods list and `resourceVersion`, then calls specifying the `resourceVersion` and watch period of 1 second.  

### __api__  
TODO  

### __front__  
TODO
