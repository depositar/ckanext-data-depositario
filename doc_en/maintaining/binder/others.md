# Other guides

## Install git-crypt

```bash
sudo apt install git-crypt
```

## Update the Gandi PAT

```bash
kubectl create secret generic gandi-credentials \
    -n cert-manager \
    --from-literal=pat='<PAT>' \
    --dry-run=client -o yaml | kubectl apply -f -
```
