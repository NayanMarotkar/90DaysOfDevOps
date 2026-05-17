 
# Day 57: Kubernetes Resources & Probes

## 1. Resource Requests vs Limits

| Aspect          | **Requests**                          | **Limits**                           |
|-----------------|---------------------------------------|--------------------------------------|
| Purpose         | Guaranteed minimum resources          | Maximum allowed resources            |
| Used by         | Scheduler (for pod placement)         | Kubelet (runtime enforcement)        |
| Overcommit      | Allowed                              | Not allowed                          |
| QoS Impact      | Affects QoS Class                     | Affects QoS Class                     |

- **Requests** = What the pod **needs** (used for scheduling)
- **Limits** = What the pod **cannot exceed**

### QoS Classes
- **Guaranteed**: Requests = Limits (all resources)
- **Burstable**: Requests < Limits (or only requests set)
- **BestEffort**: No requests or limits

---

## 2. What Happens When Limits Are Exceeded

| Resource | Behavior                  | Outcome                     | Exit Code |
|----------|---------------------------|-----------------------------|---------|
| **Memory**   | Exceeds limit             | **OOMKilled**               | 137     |
| **CPU**      | Exceeds limit             | **Throttled** (no kill)     | -       |

- Memory has **no mercy** → container is immediately killed.
- CPU is **throttled** (slowed down).

### OOMKilled Example
```yaml
Reason: OOMKilled
Exit Code: 137
