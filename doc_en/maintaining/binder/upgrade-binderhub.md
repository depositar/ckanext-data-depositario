# Upgrade BinderHub

If there are any modifications to the Helm chart,
remember to update the on-disk dependencies:

```bash
helm dependency update ./helm
```

Then apply it using `helm upgrade`:

```bash
helm upgrade --cleanup-on-fail \
    --install binderhub ./helm \
    --namespace=binderhub \
    --create-namespace \
    -f ./helm/prod.yaml \
    -f ./helm/secure.yaml \
    -f ./helm/secrets/secret.yaml
```
