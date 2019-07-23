# k8s-realtime-monitoring

## Use:
You can preview generated manifests using `kustomize`:
```bash
kustomize build overlay/$YOUR_ENV
```  

Deploy to Kubernetes using kubectl (>1.14) or apply the result of your last `kustomize build`:
```bash
kubectl.1.14 apply -k overlay/$YOUR_ENV
# or
kustomize build overlay/$YOUR_ENV | kubectl apply -f -
```


## Description:
`base` folder contains templates for resources definition.  
They only define values that are common across all environment.  

Each `overlay` subfolder defines a environment where you can deploy the app.  
Files under an environment contains `patches` to apply to the referenced template.  

`kustomization.yaml` files are used to reference `bases` with `patches`, as well as namespacing resources together and applying common labels and/or naming patterns.  


### Details
- `overlay/dev` represents a docker-for-desktop Kubernetes cluster on my machine.  

- `overlay/gke` represents is a standard Google Kubernetes Engine cluster.


### Patches
- __dev__
    - `pvc_hostpath.yaml`:  
    Patches the `storageClassName`, docker-for-desktop exposes a `StorageClass.name: hostpath` by default.  
    
    - `compute_resource.yaml`:  
    TBD: We may want to allocate less compute resources on our dev environment.

    - `service_loadbalancer.yaml`:  
        - Thanksfully docker-for-desktop allows for a `service.type: LoadBalancer`, but other local dev cluster may need `type: ClusterIP`.  
        - RethinkDB exposes an admin web panel on port `8080`, useful for a dev environment.


- __gke__
    - `pvc_standard.yaml`:  
    Patches the `storageClassName`, GKE exposes a `StorageClass.name: standard` by default.  

    - `compute_resource.yaml`:  
    TBD: We may want to allocate more compute resources on our gke environment.

    - `service_loadbalancer.yaml`:  
    Exposes the db port only on a `LoadBalancer` type service.