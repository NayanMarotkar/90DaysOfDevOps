
# Day 52: Kubernetes Namespaces & Deployments

## 1. What are Namespaces and Why Use Them?

**Namespaces** in Kubernetes are virtual clusters that provide **logical isolation** within a single physical cluster.

### Key Benefits:
- **Resource Isolation**: Separate environments (dev, staging, prod) in the same cluster.
- **Name Scoping**: You can have the same resource name (e.g., `nginx-deployment`) in different namespaces.
- **Access Control**: Combine with RBAC to restrict user/team access per namespace.
- **Resource Quotas**: Limit CPU, Memory, and object count per namespace.
- **Organization**: Clean separation of workloads for different teams or applications.

**Default Namespaces**:
- `default`
- `kube-system`
- `kube-public`
- `kube-node-lease`

---

## 2. Deployment Manifest (`nginx-deployment.yml`)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: dev
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24.0
        ports:
        - containerPort: 80
```

### Explanation of Each Section:

| Section                        | Purpose                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| `apiVersion: apps/v1`         | API version for Deployments                                            |
| `kind: Deployment`            | Object type                                                            |
| `metadata.name`               | Name of the Deployment                                                 |
| `metadata.namespace`          | Namespace where Deployment and its Pods will live                     |
| `metadata.labels`             | Labels attached to the Deployment itself                               |
| `spec.replicas`               | Desired number of Pods                                                 |
| `spec.selector.matchLabels`   | **Selector** used by Deployment to manage Pods (must match template)   |
| `spec.template`               | **Pod Template** — blueprint for creating new Pods                     |
| `spec.template.metadata.labels` | Labels applied to each Pod (must match selector)                    |
| `spec.template.spec.containers` | Container specifications (image, name, ports, resources, etc.)       |

---

## 3. Standalone Pod vs Deployment-Managed Pod Deletion

| Scenario                        | What Happens When You Delete a Pod                                      |
|--------------------------------|-------------------------------------------------------------------------|
| **Standalone Pod**             | Pod is **permanently deleted**. No recreation.                         |
| **Pod managed by Deployment**  | Deployment controller immediately creates a **new Pod** to maintain `replicas` count. |

**Demo Observed**:
```bash
kubectl delete pod nginx-deployment-5db6767747-kktzl -n dev
```
→ A new Pod (`nginx-deployment-5db6767747-kc7ht`) was automatically created.

---

## 4. Scaling a Deployment

### Imperative Scaling:
```bash
kubectl scale deployment nginx-deployment --replicas=5 -n dev
kubectl scale deployment nginx-deployment --replicas=2 -n dev
```

### Declarative Scaling:
Edit the YAML (`replicas: 5`) and run:
```bash
kubectl apply -f nginx-deployment.yml
```

**Observed Result**: Pods scaled up to 5, then scaled down to 2.

---

## 5. Rolling Updates & Rollbacks

### Updating the Image:
```bash
# Method 1: Using set image (imperative)
kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev

# Method 2: Preferred - Update YAML and apply (declarative)
kubectl apply -f nginx-deployment.yml
```

### Rollout Commands:
```bash
kubectl rollout status deployment/nginx-deployment -n dev
kubectl rollout history deployment/nginx-deployment -n dev
kubectl rollout undo deployment/nginx-deployment -n dev     # Rollback to previous revision
```

**Behavior Observed**:
- Deployment performed a rolling update.
- Rollback successfully restored previous version (`nginx:1.24.0`).

---

## 6. Commands Summary

```bash
# Namespace Management
kubectl create namespace dev
kubectl get namespaces
kubectl get pods -A

# Deployment
kubectl apply -f nginx-deployment.yml -n dev
kubectl get deploy -n dev
kubectl get pods -n dev

# Scaling & Updating
kubectl scale deployment nginx-deployment --replicas=5 -n dev
kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev

# Rollout
kubectl rollout history deployment/nginx-deployment -n dev
kubectl rollout undo deployment/nginx-deployment -n dev
```

---



**Example Output:**
```bash
NAME                    READY   STATUS    RESTARTS   AGE
nginx-deployment-xxx    1/1     Running   0          2m
nginx-deployment-yyy    1/1     Running   0          2m
nginx-deployment-zzz    1/1     Running   0          2m
```

---

## Summary (Day 52)

- Understood **Namespaces** for logical isolation.
- Learned **Deployment** structure and its self-healing capability.
- Practiced scaling, updating, and rolling back applications.
- Compared imperative vs declarative workflows.

**Next:** Services, ConfigMaps, and Secrets.

---

