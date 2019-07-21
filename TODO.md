db:
- k8s:

- src:
---
front:
- k8s:
    - everything
- src:
    - everything
---
watcher:
- k8s:
    - seperate workloads into namespaces
    - update role and rolebinding accordingly
- src:
    - write deploy and service
    - define build step
    - create kustomization for envs