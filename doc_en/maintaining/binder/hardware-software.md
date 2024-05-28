# Hardware and software

```{note}
The computing resource is provided by [Academia Sinica Grid Computing Centre][], Grant No. AS-CFII-112-103.
```

[Academia Sinica Grid Computing Centre]: https://dicos.grid.sinica.edu.tw/

## Hardware

The Binder service for depositar has the following production machines:

| Name | IP | CPU Cores | Memory | Storage |
| ---- | -- | --------- | ------ | ------- |
| iis-binderhub-1 | CP_IP / NFS_IP | 4 | 8GB | 80GB |
| iis-binderhub-2 | WORKER_IP_1 | 4 | 8GB | 80GB |
| iis-binderhub-3 | WORKER_IP_2 | 4 | 8GB | 80GB |
| iis-binderhub-4 | WORKER_IP_3 | 4 | 8GB | 80GB |

## System software

Here is a list of the system software that we are using:

| Name | OS | Roles | Services |
| ---- | -- | ----- | -------- |
| iis-binderhub-1 | Ubuntu 22.04 LTS | control-plane | Kubernetes Control Panel, NFS server |
| iis-binderhub-2 | Ubuntu 22.04 LTS | | |
| iis-binderhub-3 | Ubuntu 22.04 LTS | | |
| iis-binderhub-4 | Ubuntu 22.04 LTS | | |

## Kubernetes components

Here is a list of the components that we are using:

| Component | Implementation | Version | Notes |
| --- | --- | --- | --- |
| Kubernetes | | 1.30.1 | kubeadm, kubelet and kubectl |
| Container runtime | [containerd][] | 1.6.31 | For pulling and running built images |
| CNI plugin | [flannel][] | 0.25.1 | |
| Network load balancer | [MetalLB][] | 0.14.5 | |
| Persistent volume provisioner | [NFS Subdir External Provisioner][] | 4.0.18 | Persistent storage after pod reboot |
| X.509 certificate controller | [cert-manager][] | 1.14.5 | Let's Encrypt |
| Package manager | [Helm][] | 3.15.0 | |

[containerd]: https://containerd.io/
[flannel]: https://github.com/flannel-io/flannel
[MetalLB]: https://metallb.universe.tf/
[NFS subdir external provisioner]: https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner#kubernetes-nfs-subdir-external-provisioner
[cert-manager]: https://cert-manager.io/
[Helm]: https://helm.sh/
