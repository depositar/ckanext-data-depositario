# Deploy locally

## Prerequisites

- A [Docker Hub][] account (or alternatives, such as <https://quay.io> and <http://azurecr.io>)
- An Ubuntu 22.04 LTS installed machine
- [Install Docker Engine][] on the above machine

## Install minikube

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

```bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

```bash
sudo usermod -aG docker $USER && newgrp docker
```

```bash
minikube start
```

## Install Helm

```bash
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
```

```bash
chmod 700 get_helm.sh
```

```bash
./get_helm.sh
```

## Install BinderHub

```bash
git clone https://github.com/depositar/binder.depositar.io-deploy.git
```

```bash
cd binder.depositar.io-deploy
```

Modify the ``helm/staging.yaml``:

```{code-block} yaml
:caption: helm/staging.yaml

binderhub:
  registry:
    url: # fill this if you are not using Docker Hub
    username: <username> # fill the username of the registry
    password: <password> # fill the password of the registry
  # ...
  config:
    BinderHub:
      # ...
      image_prefix: <docker-id OR organization-name>/<prefix>- # fill the prefix of the image
```

Install the BinderHub helm chart:

```bash
helm dependency update ./helm
```

```bash
helm upgrade --cleanup-on-fail \
    --install binderhub ./helm \
    --namespace=binderhub \
    --create-namespace \
    -f ./helm/staging.yaml
```

Check pod status:

```bash
minikube kubectl -- get pods -n binderhub
```

```{code-block} none
:caption: Console output
NAME                              READY   STATUS    RESTARTS   AGE
binder-84497754cb-v726f           1/1     Running   0          108s
binderhub-image-cleaner-549wx     1/1     Running   0          108s
hub-5f6546fd74-lp874              1/1     Running   0          108s
proxy-5768c6c87c-gb9qg            1/1     Running   0          108s
user-scheduler-6b9d666f8f-88t25   1/1     Running   0          108s
user-scheduler-6b9d666f8f-t6lmf   1/1     Running   0          108s
```

Update the ``hub_url`` in the ``helm/staging.yaml`` with the IP address of the proxy-public service reported by:

```bash
minikube service proxy-public --url -n binderhub
```

Restart the cluster:

```bash
helm upgrade --cleanup-on-fail \
    --install binderhub ./helm \
    --namespace=binderhub \
    --create-namespace \
    -f ./helm/staging.yaml
```

Then visit the IP address of the binder service reported by:

```bash
minikube service binder --url -n binderhub
```

## Tear down the deployment

```bash
helm uninstall binderhub -n binderhub
```

```bash
minikube delete
```

[Docker Hub]: https://hub.docker.com/
[Install Docker Engine]: https://docs.docker.com/engine/install/ubuntu/
