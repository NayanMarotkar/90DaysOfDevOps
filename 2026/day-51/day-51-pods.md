```markdown
# Day 51: Kubernetes Pods Deep Dive

## 1. Four Required Fields of a Kubernetes Manifest

Every Kubernetes YAML/JSON manifest **must** contain these four top-level fields:

| Field       | Description                                                                 | Example                  |
|-------------|-----------------------------------------------------------------------------|--------------------------|
| `apiVersion`| Specifies the Kubernetes API version to use                                 | `apiVersion: v1`         |
| `kind`      | Defines the type of Kubernetes object being created                         | `kind: Pod`              |
| `metadata`  | Contains data that helps identify the object (name, labels, annotations, etc.) | `metadata: { name: ... }` |
| `spec`      | Describes the desired state of the object (containers, volumes, etc.)       | `spec: { containers: [...] }` |

---

## 2. Pod Manifests

### nginx-pod.yml (Declarative)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx-container
    image: nginx:latest
    ports:
    - containerPort: 80
```

### busybox-pod.yaml (Declarative)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-pod
  labels:
    app: busybox
    environment: dev
spec:
  containers:
  - name: busybox
    image: busybox:latest
    command: ["sh", "-c", "echo Hello from BusyBox && sleep 3600"]
```

### redis-pod (Imperative - created via `kubectl run`)
```bash
kubectl run redis-pod --image=redis:latest
```

**Generated YAML** (via `kubectl get pod redis-pod -o yaml`):
- Image: `redis:latest`
- Auto-generated name, labels (`run: redis-pod`), and default configurations.

---

## 3. Imperative vs Declarative Approach

| Aspect                  | **Imperative** (`kubectl run` / `kubectl create`) | **Declarative** (`kubectl apply -f`) |
|-------------------------|----------------------------------------------------|---------------------------------------|
| **Method**              | Direct commands                                    | YAML/JSON files                       |
| **Version Control**     | Hard (commands not stored easily)                  | Excellent (Git-friendly)              |
| **Reproducibility**     | Low                                                | High                                  |
| **Complexity**          | Fast for learning/testing                          | Better for production                 |
| **Updates**             | Manual recreation or `kubectl edit`                | `kubectl apply` updates object        |
| **Example**             | `kubectl run nginx --image=nginx`                  | `kubectl apply -f nginx-pod.yml`      |

**Best Practice**: Use **Declarative** (YAML) for everything in real environments.

---

## 4. Pods in Action

**Commands executed:**

```bash
kubectl apply -f nginx-pod.yml
kubectl apply -f busybox-pod.yaml
kubectl run redis-pod --image=redis:latest

kubectl get pods -o wide
kubectl get pods --show-labels
kubectl describe pod nginx-pod
kubectl logs nginx-pod
kubectl logs busybox-pod
kubectl exec -it nginx-pod -- /bin/bash
```

**Observed Behavior:**
- All pods reached `Running` state.
- Nginx served default welcome page (`curl localhost:80` inside pod).
- BusyBox printed message and slept.
- Redis started successfully.


**Example Output:**
```bash
NAME         READY   STATUS    RESTARTS   AGE     IP            NODE
nginx-pod    1/1     Running   0          18m     10.244.2.2    local-cluster-worker2
busybox-pod  1/1     Running   0          10m     10.244.1.x    local-cluster-worker
redis-pod    1/1     Running   0          8m      10.244.1.3    local-cluster-worker
```

---

## 5. What Happens When You Delete a Standalone Pod?

```bash
kubectl delete pod nginx-pod
```

**Behavior of Standalone Pods:**
- The Pod is **permanently deleted**.
- Kubernetes does **not** automatically recreate it.
- All data inside the Pod (except PersistentVolumes) is lost.
- This is why we use higher-level controllers like **Deployment**, **ReplicaSet**, or **StatefulSet** in production — they ensure desired replicas are always running.

**Contrast with Deployment:**
If a Pod is managed by a Deployment and gets deleted, the Deployment controller immediately creates a new one.

---

## Summary

- Learned core structure of Kubernetes manifests.
- Created Pods both **declaratively** and **imperatively**.
- Understood Pod lifecycle, debugging (`describe`, `logs`, `exec`), and labeling.
- Observed behavior of standalone Pods vs managed workloads.

**Next:** Deployments, ReplicaSets, and Services.
```

**To save this as `day-51-pods.md` in one command:**

```bash
cat > day-51-pods.md << 'EOF'
# Paste the entire markdown content above here
EOF
```

Just copy the full Markdown block into the heredoc and run it. Let me know if you want any section expanded!
