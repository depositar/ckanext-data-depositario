# Setup Kubernetes

```{note}
In the following guide, the ``Control Plane`` and ``Worker Node`` stand respectively for {doc}`production machines <hardware-software>` ``iis-binderhub-1`` and ``iis-binderhub-2``~``iis-binderhub-4``. Please finish the tasks for both ``Control Plane`` and ``Worker Node``.
```

## Disable swap

::::{tab-set}

:::{tab-item} Control Plane
```bash
sudo sed -i '/swap/d' /etc/fstab
```

```bash
sudo swapoff -a
```
:::

:::{tab-item} Worker Node
```bash
sudo sed -i '/swap/d' /etc/fstab
```

```bash
sudo swapoff -a
```
:::

::::

## Disable firewall

::::{tab-set}

:::{tab-item} Control Plane
```bash
sudo systemctl disable --now ufw
```
:::

:::{tab-item} Worker Node
```bash
sudo systemctl disable --now ufw
```
:::

::::

## Setup bridge traffic

::::{tab-set}

:::{tab-item} Control Plane
```bash
cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF
```

```bash
sudo modprobe overlay
```

```bash
sudo modprobe br_netfilter
```

```bash
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
EOF
```

```bash
sudo sysctl --system
```
:::

:::{tab-item} Worker Node
```bash
cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF
```

```bash
sudo modprobe overlay
```

```bash
sudo modprobe br_netfilter
```

```bash
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
EOF
```

```bash
sudo sysctl --system
```
:::

::::

## Setup NFS Storage

```{note}
For the ``NFS_IP``, ``WORKER_IP_1``, ``WORKER_IP_2``, and ``WORKER_IP_3``,
please refer to the {doc}`hardware-software`.
```

In the ``iis-binderhub-1`` machine (we reuse it to setup the NFS storage to share data between servers):

```bash
sudo apt update && sudo apt install nfs-kernel-server
```

```bash
sudo mkdir /var/nfs/general -p
```

```bash
sudo chown nobody:nogroup /var/nfs/general
```

Modify the ``/etc/exports``:

```{code-block} bash
:caption: /etc/exports

# Replace the WORKER_IP_1, WORKER_IP_2, and WORKER_IP_3
/var/nfs/general WORKER_IP_1(rw,sync,no_subtree_check) WORKER_IP_2(rw,sync,no_subtree_check) WORKER_IP_3(rw,sync,no_subtree_check)
```

```bash
sudo systemctl restart nfs-kernel-server
```

In the worker nodes (the {doc}`production machines <hardware-software>` from ``iis-binderhub-2`` to ``iis-binderhub-4``):

```bash
sudo apt update && sudo apt install nfs-common
```

```bash
sudo mkdir -p /nfs/general
```

```bash
sudo mount NFS_IP:/var/nfs/general /nfs/general
```

Modify the ``/etc/fstab``:

```{code-block} bash
:caption: /etc/fstab

# Replace the NFS_IP
NFS_IP:/var/nfs/general /nfs/general nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
```

## Install containerd

::::{tab-set}

:::{tab-item} Control Plane
```bash
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
```

```bash
sudo mkdir -p /etc/apt/keyrings
```

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
sudo apt update
```

```bash
sudo apt install containerd.io
```

```bash
containerd config default | sudo tee /etc/containerd/config.toml
```

```bash
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml
```

```bash
sudo systemctl restart containerd
```

```bash
sudo systemctl enable containerd
```
:::

:::{tab-item} Worker Node
```bash
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
```

```bash
sudo mkdir -p /etc/apt/keyrings
```

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
sudo apt update
```

```bash
sudo apt install containerd.io
```

```bash
containerd config default | sudo tee /etc/containerd/config.toml
```

```bash
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml
```

```bash
sudo systemctl restart containerd
```

```bash
sudo systemctl enable containerd
```
:::

::::

## Install Kubernetes

::::{tab-set}

:::{tab-item} Control Plane
```bash
sudo curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

```bash
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

```bash
sudo apt update
```

```bash
sudo apt install kubeadm kubelet kubectl
```
:::

:::{tab-item} Worker Node
```bash
sudo curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

```bash
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

```bash
sudo apt update
```

```bash
sudo apt install kubeadm kubelet kubectl
```
:::

::::

(initialize-cluster)=
## Initialize Kubernetes cluster

In the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1`` with IP address ``CP_IP``):

```bash
sudo kubeadm config images pull
```

```bash
sudo kubeadm init --apiserver-advertise-address=CP_IP --pod-network-cidr=10.244.0.0/16
```

Record the command provided by the initial command:

```bash
kubeadm join CP_IP:6443 --token my-secret-token \
        --discovery-token-ca-cert-hash sha256:my-secret-hash
```

Create regular user configuration for Kubernetes:

```bash
mkdir -p $HOME/.kube
```

```bash
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```

```bash
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## Install Container Network Interface (CNI)

In the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1``):

```bash
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
```

Check pod status:

```bash
kubectl get pods -n kube-flannel
```

```{code-block} none
:caption: Console output
NAME                    READY   STATUS    RESTARTS   AGE
kube-flannel-ds-f8cgz   1/1     Running   0          2m30s
```

## Join the worker nodes

```{Attention}
Please ensure that you complete all tasks related to the worker node.
```

In the worker nodes (the {doc}`production machines <hardware-software>` from ``iis-binderhub-2`` to ``iis-binderhub-4``),
run the command provided by the [initial command](#initialize-cluster):

```bash
sudo kubeadm join CP_IP:6443 --token my-secret-token \
        --discovery-token-ca-cert-hash sha256:my-secret-hash
```

## Install Load Balancer

In the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1``):

```bash
MetalLB_RTAG=$(curl -s https://api.github.com/repos/metallb/metallb/releases/latest|grep tag_name|cut -d '"' -f 4|sed 's/v//')
```

```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v$MetalLB_RTAG/config/manifests/metallb-native.yaml
```

Check pod status:

```bash
kubectl get pods -n metallb-system
```

```{code-block} none
:caption: Console output
NAME                          READY   STATUS    RESTARTS   AGE
controller-86f5578878-btx4m   1/1     Running   0          80m
speaker-87m8t                 1/1     Running   0          80m
speaker-l49d7                 1/1     Running   0          2m43s
```

Create a file called ``ipaddress_pools.yaml``:

```{note}
For the ``CP_IP``, ``WORKER_IP_1``, ``WORKER_IP_2``, and ``WORKER_IP_3``,
please refer to the {doc}`hardware-software`.
```

```{code-block} yaml
:caption: ipaddress_pools.yaml

apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: production
  namespace: metallb-system
spec:
  addresses: # at least one address for ingress-nginx
  - CP_IP/32
  - WORKER_IP_1/32
  - WORKER_IP_2/32
  - WORKER_IP_3/32
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2-advert
  namespace: metallb-system
```

```bash
kubectl apply -f ipaddress_pools.yaml
```

## Install Helm

In the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1``):

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
```

```bash
chmod 700 get_helm.sh
```

```bash
./get_helm.sh
```

## Install NFS provisioner

In the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1``  with IP address ``NFS_IP``):

```bash
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
```

```bash
helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
--set nfs.server=NFS_IP \
--set nfs.path=/var/nfs/general
```

```bash
kubectl patch storageclass nfs-client -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

Check pod status:

```bash
kubectl get pods -n default
```

```{code-block} none
:caption: Console output
NAME                                               READY   STATUS    RESTARTS   AGE
nfs-subdir-external-provisioner-7fd7884cbc-lt7v8   1/1     Running   0          57s
```
