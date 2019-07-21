__db__:
- _k8s_:

- _src_:
---
__front__:
- _k8s_:
    - everything
- _src_:
    - everything
---
__watcher__:
- _k8s_:
    - seperate workloads into namespaces
    - update role and rolebinding accordingly
- _src_:
    - write deploy and service
    - define build step
    - create kustomization for envs