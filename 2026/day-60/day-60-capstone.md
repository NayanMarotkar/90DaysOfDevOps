
# Day 60: Kubernetes Capstone Project - WordPress + MySQL

## Project Architecture

### Components Overview

- **Namespace**: `capstone` (isolates the entire project)
- **MySQL (Stateful)**:
  - StatefulSet (`mysql`)
  - Headless Service (`mysql`)
  - PersistentVolumeClaim (`mysql-data`)
  - Secret (`mysql-secret`)
- **WordPress (Stateless)**:
  - Deployment (`wordpress`) with 2 replicas
  - NodePort Service (`wordpress-nodeport`)
  - ConfigMap (`wordpress-config`)
  - HPA (`wordpress-hpa`)

### Connection Flow

Browser → NodePort Service (30080) → WordPress Pods (Deployment)
↓
WORDPRESS_DB_HOST → mysql-0.mysql.capstone.svc.cluster.local:3306
↓
Headless Service → MySQL StatefulSet
↓
PersistentVolume (MySQL data)


**Key Environment Variables**:
- WordPress uses `ConfigMap` + `Secret` to connect securely to MySQL.

---

## Self-Healing & Persistence Test Results

| Test                        | Action                        | Result                          | Observation                     |
|----------------------------|-------------------------------|---------------------------------|---------------------------------|
| WordPress Self-Healing     | Deleted WordPress pod         | Recreated automatically        | Site remained accessible       |
| MySQL Self-Healing         | Deleted `mysql-0` pod         | Recreated by StatefulSet       | Took 30-90 seconds             |
| Data Persistence           | Deleted MySQL pod             | Blog post still available      | Data survived thanks to PVC    |

**Conclusion**: Self-healing worked perfectly. Data persistence was successful.

---

## Concepts Used in This Project

| Concept                    | Learned On     | Used In                  |
|---------------------------|----------------|--------------------------|
| Namespace                 | Day 52         | `capstone`               |
| Secret                    | Day 54         | MySQL credentials        |
| ConfigMap                 | Day 54         | WordPress configuration  |
| PersistentVolumeClaim     | Day 55         | MySQL storage            |
| StatefulSet               | Day 56         | MySQL database           |
| Headless Service          | Day 56         | MySQL stable networking  |
| Deployment                | Day 52         | WordPress                |
| Service (NodePort)        | Day 53         | External access          |
| Resource Requests/Limits  | Day 52         | Both applications        |
| Liveness & Readiness Probes | Day 52       | WordPress                |
| HorizontalPodAutoscaler   | Day 57         | WordPress scaling        |
| Helm                      | Day 59         | Previous exercises       |

---

## Reflection

### What was Hardest?
- Understanding **StatefulSet** vs Deployment and why MySQL needs a Headless Service + PVC.
- Getting the correct `WORDPRESS_DB_HOST` format for service discovery.
- Debugging pod readiness when MySQL was still initializing.

### What Clicked?
- The power of **declarative YAML** and how one `kubectl apply` can manage complex applications.
- How **Namespaces** cleanly isolate projects.
- The beauty of **self-healing** and persistence in Kubernetes.

### What I Would Add for Production:
- Ingress + TLS (Let's Encrypt)
- WordPress PersistentVolume for `/var/www/html/wp-content`
- Database connection pooling / Redis caching
- Proper secrets management (External Secrets Operator or Vault)
- Monitoring (Prometheus + Grafana)
- Backup strategy for PVC
- Helm Chart packaging for the entire stack
- NetworkPolicy for security

---

