_current_dir = $(shell pwd)

_OVERLAYS=${_current_dir}/k8s/overlays
_K8S_DEV=${_OVERLAYS}/dev
_K8S_GKE=${_OVERLAYS}/gke

deploy-local:
	kustomize build ${_K8S_DEV}

deploy-gke:
	kustomize build ${_K8S_GKE}