
# Day 55: Persistent Volumes (PV) and Persistent Volume Claims (PVC) in Kubernetes

## Why Containers Need Persistent Storage

By default, containers are **ephemeral**:
- Data written inside a container is lost when the container crashes or is restarted.
- `emptyDir` volumes are deleted when the Pod is deleted or rescheduled.

**Persistent Storage** is required when your application needs to:
- Store user data, databases, logs, or uploaded files
- Survive pod restarts, deletions, or rescheduling to other nodes
- Maintain state across deployments

---

## What are PV and PVC?

### **PersistentVolume (PV)**
- A cluster-wide resource that represents actual storage (physical or cloud volume).
- Created by cluster administrators or dynamically by StorageClasses.
- Defines storage capacity, access modes, and reclaim policy.

### **PersistentVolumeClaim (PVC)**
- A request for storage by a user (developer).
- Pods consume storage **via PVC**, not directly via PV.
- Kubernetes binds a suitable PV to the PVC.

**Relationship**: PVC is like a "ticket" to use a PV. One PVC binds to exactly one PV.

---

## Static vs Dynamic Provisioning

| Feature                  | Static Provisioning                  | Dynamic Provisioning                      |
|-------------------------|--------------------------------------|-------------------------------------------|
| How PV is created       | Manually by admin                    | Automatically by StorageClass             |
| Use Case                | Learning, specific storage control   | Production, cloud environments            |
| Flexibility             | Less flexible                        | Highly flexible                           |
| StorageClassName        | Usually empty (`""`)                 | Specified (e.g., `standard`)              |

**Dynamic Provisioning** is the recommended approach in production.

---

## Access Modes

| Access Mode      | Short | Description                                      | Common Use Case          |
|------------------|-------|--------------------------------------------------|--------------------------|
| ReadWriteOnce    | RWO   | Read-write by a single node                      | Databases, most apps     |
| ReadOnlyMany     | ROX   | Read-only by many nodes                          | Shared config            |
| ReadWriteMany    | RWX   | Read-write by many nodes                         | Shared file systems      |

---

## Reclaim Policies

| Reclaim Policy | Behavior when PVC is deleted                          | Use Case                        |
|----------------|-------------------------------------------------------|---------------------------------|
| **Delete**     | PV and underlying storage are automatically deleted   | Cloud storage (default)         |
| **Retain**     | PV remains (status → Released)                        | Protect important data          |
| **Recycle**    | Deprecated                                            | Old method                      |

---

## Summary of Key Concepts

- **emptyDir** → Temporary storage (lost on pod deletion)
- **PV** → Actual storage resource in the cluster
- **PVC** → User’s request for storage
- **StorageClass** → Enables dynamic provisioning
- Use **PVC** in Pods via `volumeMounts`
- Choose **Reclaim Policy** carefully based on data importance

---

**Best Practices:**
- Always use PVCs instead of directly referencing PVs
- Prefer Dynamic Provisioning with proper StorageClass
- Use `Retain` policy for critical data
- Monitor storage usage regularly

---
