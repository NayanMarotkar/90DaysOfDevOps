
# Day 58: Metrics Server & Horizontal Pod Autoscaler (HPA)

## 1. What is Metrics Server?

**Metrics Server** is a Kubernetes add-on that collects resource usage data (CPU & Memory) from Kubelets on each node.

- It polls metrics from all nodes every ~15 seconds.
- Provides data for `kubectl top` command.
- **Essential for Horizontal Pod Autoscaler (HPA)** — without it, HPA cannot fetch real CPU/Memory usage.

> **Note**: Metrics Server is **not** installed by default in Kind or kubeadm clusters.

### Why HPA Needs Metrics Server
HPA needs real-time resource utilization to decide how many replicas to run. Without Metrics Server, HPA shows `<unknown>` in the TARGETS column.

---

## 2. How HPA Calculates Desired Replicas

**Formula** (for CPU metric):
desiredReplicas = ceil[ currentReplicas * (currentMetricValue / desiredMetricValue) ]


**Example**:
- Current replicas: 2
- Current average CPU: 120m
- Requested CPU per pod: 200m
- Target utilization: 50% → desiredMetricValue = 100m
- Calculation: `2 * (120 / 100) = 2.4` → rounded up to **3 replicas**

---

## 3. autoscaling/v1 vs autoscaling/v2

| Feature                        | **autoscaling/v1**          | **autoscaling/v2**                     |
|--------------------------------|-----------------------------|----------------------------------------|
| Metrics Supported              | Only CPU                    | CPU, Memory, Custom Metrics            |
| Multiple Metrics               | No                          | Yes                                    |
| Scaling Behavior Control       | No                          | Yes (`behavior` section)               |
| External Metrics               | No                          | Yes                                    |
| Recommended                    | Legacy                      | **Modern & Recommended**               |

---

## 4. Important Commands

```bash
# Real-time usage
kubectl top nodes
kubectl top pods -A --sort-by=cpu

# HPA status
kubectl get hpa
kubectl describe hpa php-apache

# Watch scaling live
kubectl get hpa php-apache --watch
kubectl get pods -l run=php-apache --watch

5. Typical Outputs / "Screenshots" Reference
kubectl top pods --sort-by=cpu

NAME                          CPU(cores)   MEMORY(bytes)
php-apache-abc12-xyz          245m         28Mi
load-generator                15m          8Mi

HPA during load

NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   78%/50%   1         10        5          4m

Events from kubectl describe hpa

Scaled up from 1 to 4
Scaled down from 5 to 2


