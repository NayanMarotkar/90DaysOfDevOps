# Day 56: Kubernetes StatefulSets

## What are StatefulSets?

**StatefulSet** is a Kubernetes workload API object used to manage **stateful applications**.

It provides:
- Stable, unique network identity (pod name + DNS)
- Stable persistent storage
- Ordered deployment, scaling, and deletion
- Sticky identity for each pod

### When to use StatefulSet vs Deployment?

| Feature                    | Deployment                          | StatefulSet                              |
|---------------------------|-------------------------------------|------------------------------------------|
| Pod Identity              | Ephemeral (random names)            | Stable (web-0, web-1, web-2)            |
| DNS Resolution            | Single Service IP (Load Balanced)   | Individual DNS per pod (Headless)       |
| Storage                   | Shared or ephemeral                 | Persistent per pod (volumeClaimTemplates)|
| Scaling Order             | No guarantee                        | Ordered (0 → 1 → 2)                     |
| Termination Order         | No guarantee                        | Reverse order (2 → 1 → 0)               |
| Use Cases                 | Stateless apps (Nginx, API servers) | Databases (MySQL, PostgreSQL, MongoDB, Redis), Kafka, ZooKeeper, Elasticsearch |
| Pod Replacement           | New pod gets new identity           | New pod re-attaches same identity + storage |

**Rule of Thumb**:
- Use **Deployment** for stateless applications.
- Use **StatefulSet** when pods need **stable identity** or **persistent storage**.

## Key Components of StatefulSet

### 1. Headless Service
- Created with `clusterIP: None`
- Required by StatefulSet for stable DNS
- Does **not** provide load balancing
- Each pod gets its own DNS entry

**Example DNS Format:**

Example: `web-0.myapp-headless.default.svc.cluster.local`

### 2. Stable Network Identity
- Pods maintain the same hostname even after restart or rescheduling.
- DNS resolution always points to the same pod IP.

### 3. volumeClaimTemplates
- Automatically creates PersistentVolumeClaim (PVC) for **each pod**.
- PVC naming: `<volume-name>-<pod-name>`
- When a pod is deleted and recreated, it re-attaches to the **same PVC** → data persists.

## Lab Summary

### Pods Created
- `web-0`
- `web-1`
- `web-2`
- `web-3`
- `web-4` (during scale up)

### PVCs Created
- `data-web-0`
- `data-web-1`
- `data-web-2`
- `data-web-3`
- `data-web-4`

**Important Observation**:  
PVCs are **not** deleted when StatefulSet is deleted. You must delete them manually.

## Screenshots / Command Outputs

### 1. Pods
```bash
kubectl get pods -o wide
