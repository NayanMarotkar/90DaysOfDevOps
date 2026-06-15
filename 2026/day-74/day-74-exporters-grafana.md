# Day 74 — Exporters & Grafana

## Overview

Today I expanded my observability stack by adding exporters and Grafana for visualization.

I deployed Node Exporter for host-level monitoring, cAdvisor for container-level monitoring, and Grafana for dashboarding. I also configured Prometheus to scrape metrics from all exporters and learned how Grafana datasource provisioning works through YAML.

By the end of the day, I had a complete monitoring stack capable of collecting and visualizing infrastructure and container metrics in real time.

---

# Architecture

```text
                           +------------------+
                           |     Grafana      |
                           +---------+--------+
                                     |
                                     |
                                     v
                           +------------------+
                           |    Prometheus    |
                           +---------+--------+
                                     |
          +--------------------------+--------------------------+
          |                                                     |
          v                                                     v

+----------------------+                          +----------------------+
|    Node Exporter     |                          |      cAdvisor        |
+----------------------+                          +----------------------+
          |                                                     |
          v                                                     v

     Host Metrics                                    Container Metrics

  CPU Usage                                         Container CPU Usage
  Memory Usage                                      Container Memory Usage
  Disk Usage                                        Container Network Usage
  Network Statistics                               Container Filesystem Usage
```

---

# Docker Compose Configuration

## docker-compose.yml

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    restart: unless-stopped
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    restart: unless-stopped
    networks:
      - monitoring

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:rw
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    restart: unless-stopped
    networks:
      - monitoring

  grafana:
    image: grafana/grafana-enterprise:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    restart: unless-stopped
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
```

---

# Prometheus Configuration

## prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["prometheus:9090"]

  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "cadvisor"
    static_configs:
      - targets: ["cadvisor:8080"]
```

---

# Node Exporter vs cAdvisor

Both exporters expose metrics for Prometheus but monitor different layers of the system.

| Feature         | Node Exporter   | cAdvisor             |
| --------------- | --------------- | -------------------- |
| Scope           | Host Level      | Container Level      |
| Monitors        | Linux Server    | Docker Containers    |
| CPU Metrics     | Host CPU        | Per-Container CPU    |
| Memory Metrics  | Host Memory     | Per-Container Memory |
| Disk Metrics    | Host Filesystem | Container Filesystem |
| Network Metrics | Host Network    | Container Network    |
| Default Port    | 9100            | 8080                 |

### When to Use Node Exporter

Use Node Exporter when monitoring:

* CPU utilization of the server
* Memory usage
* Disk usage
* Filesystem health
* Network throughput

Example Metrics:

```promql
node_cpu_seconds_total
node_memory_MemAvailable_bytes
node_filesystem_avail_bytes
```

### When to Use cAdvisor

Use cAdvisor when monitoring:

* Docker container CPU usage
* Container memory consumption
* Container network traffic
* Container filesystem usage

Example Metrics:

```promql
container_cpu_usage_seconds_total
container_memory_usage_bytes
container_network_receive_bytes_total
```

---

# Prometheus Targets

Prometheus successfully scraped all configured targets.

| Target        | Status |
| ------------- | ------ |
| Prometheus    | UP     |
| Node Exporter | UP     |
| cAdvisor      | UP     |

### Screenshot

Add screenshot:


<img width="1919" height="932" alt="image" src="https://github.com/user-attachments/assets/4b79edfe-145f-4ca5-865c-7d11f67fbdc5" />
<img width="1912" height="305" alt="image" src="https://github.com/user-attachments/assets/6d1c17b7-8e27-4b95-baf7-f3be152fe145" />



---

# Custom Grafana Dashboard

Created a custom dashboard containing:

* CPU Usage
* Memory Usage
* Disk Usage
* Container CPU Usage
* Container Memory Usage

### Screenshot


<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/fce7d34a-40fe-48ef-94bf-7ddcb7bad175" />

```
---

# Imported Node Exporter Dashboard

Imported Grafana Dashboard ID:

```text
1860
```

Dashboard Name:


<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/ad94723d-995b-4f78-91da-55a22f3797a9" />

```

This dashboard provides:

* CPU Utilization
* Memory Usage
* Disk Usage
* Filesystem Statistics
* Network Traffic
* System Load

### Screenshot

<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/866a36a2-340c-4631-9096-110bae33b80b" />



---

# PromQL Queries

## CPU Usage

```promql
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

Returns host CPU utilization percentage.

---

## Memory Usage

```promql
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes)
/
node_memory_MemTotal_bytes * 100
```

Returns memory usage percentage.

---

## Disk Usage

```promql
100 - (
node_filesystem_avail_bytes{mountpoint="/"}
/
node_filesystem_size_bytes{mountpoint="/"}
) * 100
```

Returns disk utilization percentage.

---

## Container CPU Usage

```promql
rate(container_cpu_usage_seconds_total[5m])
```

Returns container CPU consumption rate.

---

## Container Memory Usage

```promql
container_memory_usage_bytes
```

Returns memory consumed by running containers.

---

# Grafana Datasource Provisioning

Datasource provisioning allows Grafana to automatically configure data sources at startup using YAML files.

Benefits:

* Infrastructure as Code
* No Manual Configuration
* Consistent Deployments
* Easy Automation

## Datasource Configuration

File:

```text
grafana/provisioning/datasources/prometheus.yml
```

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
```

## How It Works

1. Grafana starts.
2. Reads YAML files from the provisioning directory.
3. Creates the Prometheus datasource automatically.
4. Marks it as the default datasource.
5. Dashboards can immediately query Prometheus metrics.

---

# Key Takeaways

* Learned the difference between host monitoring and container monitoring.
* Used Node Exporter to collect Linux host metrics.
* Used cAdvisor to collect Docker container metrics.
* Connected Grafana to Prometheus.
* Created custom dashboards for infrastructure monitoring.
* Imported the Node Exporter Full dashboard (ID 1860).
* Practiced PromQL for CPU, memory, disk, and container metrics.
* Automated Grafana datasource creation using YAML provisioning.

This setup provides complete visibility into both the host system and running containers, forming the foundation for centralized logging and distributed tracing in upcoming observability challenges.
