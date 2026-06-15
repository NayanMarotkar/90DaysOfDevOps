# Day 75 — Log Management with Loki & Promtail

## Overview

Today I implemented the second pillar of observability: **Logs**.

While Prometheus provides metrics that tell us *what* is happening, logs provide detailed information that helps explain *why* something happened.

I deployed Grafana Loki as a centralized log storage backend and Promtail as a log collection agent. Promtail collects Docker container logs and ships them to Loki, while Grafana provides a unified interface for querying and visualizing logs alongside metrics.

By the end of the day, I had a complete logging pipeline integrated with my existing monitoring stack.

---

# Architecture

```text
+----------------------+
| Docker Containers    |
+----------+-----------+
           |
           |
           v
+----------------------+
|      Promtail        |
| (Log Collection)     |
+----------+-----------+
           |
           |
           v
+----------------------+
|        Loki          |
|  (Log Storage)       |
+----------+-----------+
           |
           |
           v
+----------------------+
|      Grafana         |
| (Logs & Metrics UI)  |
+----------+-----------+
           |
           |
           v
+----------------------+
|        User          |
+----------------------+
```

---

# Understanding the Logging Pipeline

Docker containers generate logs and store them as JSON files on the host.

Promtail continuously reads these log files, adds labels, and forwards the logs to Loki.

Loki stores logs efficiently by indexing only labels rather than the entire log content.

Grafana queries Loki using LogQL and displays logs through Explore and dashboard panels.

---

# Why Loki Only Indexes Labels

Unlike Elasticsearch, Loki does not index the entire log message.

Instead, it indexes only metadata labels such as:

* Container Name
* Job Name
* Namespace
* Application

Benefits:

* Lower storage usage
* Lower memory consumption
* Faster ingestion
* Easier operations

Trade-Off:

* Full-text searching is less powerful than Elasticsearch.
* Queries rely heavily on labels.

This design makes Loki significantly cheaper and simpler to operate than a traditional ELK stack.

---

# Loki Configuration

## loki/loki-config.yml

```yaml
auth_enabled: false

server:
  http_listen_port: 3100

common:
  ring:
    instance_addr: 127.0.0.1
    kvstore:
      store: inmemory
  replication_factor: 1
  path_prefix: /loki

schema_config:
  configs:
    - from: 2020-10-24
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

storage_config:
  filesystem:
    directory: /loki/chunks
```

### Explanation

| Setting                  | Purpose                    |
| ------------------------ | -------------------------- |
| auth_enabled             | Disables authentication    |
| http_listen_port         | Loki API port              |
| replication_factor       | Single instance deployment |
| store: tsdb              | Uses Loki TSDB storage     |
| object_store: filesystem | Stores chunks locally      |
| directory                | Location of log storage    |

---

# Promtail Configuration

## promtail/promtail-config.yml

```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: docker
    static_configs:
      - targets:
          - localhost
        labels:
          job: docker
          __path__: /var/lib/docker/containers/*/*-json.log

    pipeline_stages:
      - docker: {}
```

### Explanation

| Setting         | Purpose                     |
| --------------- | --------------------------- |
| positions       | Tracks log reading progress |
| clients         | Loki endpoint               |
| **path**        | Docker log file location    |
| pipeline_stages | Parses Docker JSON logs     |

---

# Updated Docker Compose Configuration

## docker-compose.yml

```yaml
services:
  prometheus:
    image: prom/prometheus:latest

  node-exporter:
    image: prom/node-exporter:latest

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest

  grafana:
    image: grafana/grafana-enterprise:latest

  loki:
    image: grafana/loki:latest
    container_name: loki
    ports:
      - "3100:3100"
    volumes:
      - ./loki/loki-config.yml:/etc/loki/loki-config.yml
      - loki_data:/loki
    command: -config.file=/etc/loki/loki-config.yml
    restart: unless-stopped

  promtail:
    image: grafana/promtail:latest
    container_name: promtail
    volumes:
      - ./promtail/promtail-config.yml:/etc/promtail/promtail-config.yml
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock
    command: -config.file=/etc/promtail/promtail-config.yml
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
  loki_data:
```

---

# Grafana Datasource Provisioning

## datasources.yml

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true

  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
```

After restarting Grafana, both Prometheus and Loki were automatically configured as datasources.

---

# LogQL Queries

## 1. View All Docker Logs

```logql
{job="docker"}
```

Returns all logs collected by Promtail.

---

## 2. Search for Errors

```logql
{job="docker"} |= "error"
```

Returns log lines containing the word "error".

---

## 3. Exclude Health Check Logs

```logql
{job="docker"} != "health"
```

Filters out health check noise.

---

## 4. Count Logs Over Time

```logql
count_over_time({job="docker"}[5m])
```

Returns total log lines generated over the last five minutes.

---

## 5. Log Rate

```logql
rate({job="docker"}[5m])
```

Returns logs per second.

---

# Exercise Solutions

## Find Error Logs From notes-app

```logql
{container_name="notes-app"} |= "error"
```

Returns all error log entries from the notes-app container.

---

## Count Error Logs Per Minute

```logql
count_over_time({container_name="notes-app"} |= "error" [1m])
```

Returns the number of error logs generated per minute.

---

# Metrics and Logs Correlation

One of the biggest advantages of Grafana is having both metrics and logs in a single platform.

Example Workflow:

1. Detect a CPU spike using Prometheus metrics.
2. Click the spike timestamp.
3. Open logs for the same timeframe.
4. Identify the application error causing the spike.

This drastically reduces troubleshooting time compared to switching between separate monitoring and logging tools.

---

# Screenshot: Grafana Explore

Add Screenshot:


<img width="1919" height="839" alt="image" src="https://github.com/user-attachments/assets/1b9a9976-abce-48ef-b68a-6d45cb575432" />

```

Shows Docker container logs being queried through Loki.

---

# Screenshot: Metrics and Logs Side by Side

Add Screenshot:

```text
screenshots/grafana-metrics-logs-correlation.png
```

Shows Prometheus metrics and Loki logs displayed simultaneously in Grafana Explore split view.

---

# Loki vs ELK Stack

| Feature               | Loki      | ELK Stack |
| --------------------- | --------- | --------- |
| Storage Cost          | Low       | High      |
| Memory Usage          | Low       | High      |
| Setup Complexity      | Simple    | Complex   |
| Full Text Search      | Limited   | Excellent |
| Kubernetes Friendly   | Excellent | Good      |
| Resource Requirements | Low       | High      |
| Label-Based Queries   | Yes       | No        |

---

## When to Use Loki

Choose Loki when:

* Running Grafana already
* Monitoring containers or Kubernetes
* Cost efficiency is important
* Label-based searches are sufficient

Examples:

* DevOps environments
* Small to medium platforms
* Kubernetes clusters

---

## When to Use ELK

Choose ELK when:

* Advanced full-text search is required
* Massive log analytics workloads exist
* Complex search patterns are needed

Examples:

* Security operations
* Compliance auditing
* Enterprise log analytics

---

# Key Takeaways

* Learned the second pillar of observability: Logs.
* Deployed Loki as a centralized log storage backend.
* Deployed Promtail to collect Docker container logs.
* Added Loki as a Grafana datasource.
* Queried logs using LogQL.
* Correlated metrics and logs in Grafana.
* Learned the differences between Loki and ELK.
* Built a complete monitoring and logging platform using Prometheus, Grafana, Loki, Promtail, Node Exporter, and cAdvisor.

The observability stack now includes both metrics and logs, laying the foundation for distributed tracing with OpenTelemetry in the next phase.
