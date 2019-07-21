## Per-service TODO

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
    - define build steps (Makefile + update spec.template images)
    - create kustomization for envs
    - centralize variables in a configMapGenerator
