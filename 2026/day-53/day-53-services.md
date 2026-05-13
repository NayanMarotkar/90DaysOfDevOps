
# Day 53: Kubernetes Services

## 1. What Problem Do Services Solve?

**Kubernetes Services** provide a **stable networking abstraction** for a set of Pods.

### Problems They Solve:
- Pods are **ephemeral** — they can die, restart, or be rescheduled with **new IPs**.
- Direct Pod IPs are unstable and hard to manage.
- Clients (other Pods or external users) need a consistent way to reach the application.

### Relationship with Pods & Deployments:
- A **Service** selects Pods using **labels** (`selector`).
- It provides a **virtual IP** (Cluster IP) and DNS name.
- When used with a **Deployment**, the Service automatically load-balances traffic across all healthy Pods (replicas).

---

## 2. Three Service Manifests

### 1. ClusterIP Service (`clusterip-service.yml`)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-clusterip
spec:
  type: ClusterIP
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
```

### 2. NodePort Service (`nodeport-service.yml`)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-nodeport
spec:
  type: NodePort
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

### 3. LoadBalancer Service (`loadbalancer-service.yml`)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
```

---

## 3. Difference Between Service Types

| Service Type       | Scope                  | Access Method                          | Typical Use Case                     | External IP     |
|--------------------|------------------------|----------------------------------------|--------------------------------------|-----------------|
| **ClusterIP**      | Internal only          | Via Cluster IP + DNS                   | Internal microservices communication | None            |
| **NodePort**       | Cluster + External     | `<NodeIP>:<NodePort>` (30000–32767)   | Quick external testing / dev         | Node IPs        |
| **LoadBalancer**   | External (Cloud)       | Provisioned cloud load balancer        | Production web apps on cloud         | Yes (cloud LB)  |

**Demo Results**:
- **ClusterIP**: `10.96.86.184`
- **NodePort**: Accessible at `172.18.0.3:30080`
- **LoadBalancer**: `EXTERNAL-IP: <pending>` (expected in Kind/minikube without cloud provider)

---

## 4. Kubernetes DNS for Service Discovery

Kubernetes runs **CoreDNS** in the `kube-system` namespace.

### DNS Format:
```
<service-name>.<namespace>.svc.cluster.local
```

**Examples**:
- `web-app-clusterip.default.svc.cluster.local`
- Short form inside same namespace: `web-app-clusterip`

**Tested**:
```bash
wget -qO- http://web-app-clusterip
wget -qO- http://web-app-clusterip.default.svc.cluster.local
nslookup web-app-clusterip
```

---

## 5. What are Endpoints?

**Endpoints** is a Kubernetes object that contains the **actual IP addresses and ports** of the Pods selected by a Service.

- The Service acts as a **load balancer** in front of these Endpoints.
- Kubernetes automatically updates Endpoints when Pods are added/removed.

**How to Inspect**:
```bash
kubectl get endpoints web-app-clusterip
kubectl describe service web-app-clusterip
```

**Observed in describe output**:
```
Endpoints: 10.244.1.2:80,10.244.1.3:80,10.244.2.2:80
```

---

## 6. Deployment Used

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  labels:
    app: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
```

---

**Example Output:**
```bash
NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)
web-app-clusterip      ClusterIP      10.96.86.184     <none>        80/TCP
web-app-nodeport       NodePort       10.96.101.250    <none>        80:30080/TCP
web-app-loadbalancer   LoadBalancer   10.96.4.248      <pending>     80:31962/TCP
```

**Successful Test**:
- Internal access via ClusterIP (from busybox test pod)
- External access via NodePort using node IP
- DNS resolution working

---

## Summary (Day 53)

- Services provide **stable networking** and **load balancing** for Pods.
- Learned **ClusterIP**, **NodePort**, and **LoadBalancer** types.
- Understood Kubernetes DNS and Endpoints.
- Successfully exposed a 3-replica Nginx Deployment.

**Next:** Ingress, ConfigMaps & Secrets.

---
