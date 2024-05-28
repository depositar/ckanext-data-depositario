# Install BinderHub

```{hint}
The images built by the Binder service are pushed to a private [Harbor][] registry.
The repository for configuration files: <https://github.com/depositar/binder.depositar.io-deploy> already includes the credentials for the registry.
```

```{note}
The tasks below should be finished in the Control Plane (the {doc}`production machine <hardware-software>` ``iis-binderhub-1``).
```

## Install the helm chart

```bash
git clone https://github.com/depositar/binder.depositar.io-deploy.git
```

```bash
cd binder.depositar.io-deploy
```

{doc}`Install git-crypt <others>` and decrypt the secrets:

```bash
git-crypt unlock git_crypt_secret_key
```

```{tip}
The git-crypt symmetric key ``git_crypt_secret_key`` is required to decrypt the secrets.
Contact a system administrator if you need access to the git-crypt key.
```

Update the on-disk dependencies:

```bash
helm dependency update ./helm
```

Install BinderHub:

```bash
helm upgrade --cleanup-on-fail \
    --install binderhub ./helm \
    --namespace=binderhub \
    --create-namespace \
    -f ./helm/prod.yaml \
    -f ./helm/secrets/secret.yaml
```

Check pod status:

```bash
kubectl get pods -n binderhub
```

```{code-block} none
:caption: Console output
NAME                                                  READY   STATUS    RESTARTS   AGE
binder-5449d5ff5b-2w9x9                               1/1     Running   0          56s
binderhub-dind-9bfmv                                  1/1     Running   0          56s
binderhub-image-cleaner-kj26v                         1/1     Running   0          56s
binderhub-ingress-nginx-controller-5bd9459f5b-ckx7b   1/1     Running   0          56s
hub-6b9d7f7f8-wm6vp                                   1/1     Running   0          56s
proxy-6b9bd4c4c5-pbk96                                1/1     Running   0          56s
user-scheduler-6b9d666f8f-b82dt                       1/1     Running   0          56s
user-scheduler-6b9d666f8f-nvpn6                       1/1     Running   0          56s
```

Then visit <http://binder.depositar.io>.

## Secure with HTTPS

Install cert-manager:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.5/cert-manager.yaml
```

Check pod status:

```bash
kubectl get pods -n cert-manager
```

```{code-block} none
:caption: Console output
NAME                                       READY   STATUS    RESTARTS      AGE
cert-manager-cainjector-65c7bff89d-hh57j   1/1     Running   0             10s
cert-manager-cbcf9668d-sf55h               1/1     Running   0             10s
cert-manager-webhook-594cb9799b-vmlf2      1/1     Running   0             10s
```

Update BinderHub with HTTPS:

```bash
helm upgrade --cleanup-on-fail \
    --install binderhub ./helm \
    --namespace=binderhub \
    --create-namespace \
    -f ./helm/prod.yaml \
    -f ./helm/secure.yaml \
    -f ./helm/secrets/secret.yaml
```

Then visit <https://binder.depositar.io>.

[Harbor]: https://goharbor.io/
