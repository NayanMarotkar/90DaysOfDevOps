# Day 76 — OpenTelemetry & Alerting

## Overview

Today I completed the third pillar of observability by implementing **Distributed Tracing** using the OpenTelemetry Collector and configured both **Prometheus Alerting** and **Grafana Alerting**.

Until now, my observability stack included:

* Metrics (Prometheus, Node Exporter, cAdvisor)
* Logs (Loki, Promtail)

Today I added:

* OpenTelemetry Collector
* OTLP Receivers
* Trace Collection
* Prometheus Alert Rules
* Grafana Alert Rules
* Notification Policies

The platform can now collect, process, visualize, and alert on metrics, logs, and traces.

---

# OpenTelemetry Architecture

OpenTelemetry follows a pipeline model consisting of:

```text
Applications
      |
      v
  Receivers
      |
      v
 Processors
      |
      v
 Exporters
      |
      v
 Observability Backends
```

---

## Receivers

Receivers accept telemetry data from applications.

Examples:

* OTLP
* Prometheus
* Jaeger
* Zipkin

In this project:

```yaml
receivers:
  otlp:
```

Accepted telemetry via:

* gRPC (4317)
* HTTP (4318)

---

## Processors

Processors modify telemetry before exporting.

Examples:

* Batching
* Sampling
* Filtering

In this project:

```yaml
processors:
  batch:
```

Benefits:

* Reduces network overhead
* Improves throughput
* Improves performance

---

## Exporters

Exporters send telemetry to destinations.

Examples:

* Prometheus
* Loki
* Jaeger
* Tempo
* Datadog

In this project:

```yaml
exporters:
  prometheus:
  debug:
```

Metrics are exported to Prometheus.

Logs and traces are exported to the debug console.

---

# OpenTelemetry Collector Configuration

## otel-collector/otel-collector-config.yml

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"

  debug:
    verbosity: detailed

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]

    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]

    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]
```

---

# Configuration Explanation

## OTLP Receiver

```yaml
receivers:
  otlp:
```

Receives telemetry data using the OpenTelemetry Protocol.

Supported Ports:

| Protocol  | Port |
| --------- | ---- |
| OTLP gRPC | 4317 |
| OTLP HTTP | 4318 |

---

## Batch Processor

```yaml
processors:
  batch:
```

Groups telemetry before exporting.

Benefits:

* Fewer network requests
* Better scalability
* Higher throughput

---

## Prometheus Exporter

```yaml
exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"
```

Exposes metrics for Prometheus scraping.

Prometheus target:

```text
otel-collector:8889
```

---

## Debug Exporter

```yaml
exporters:
  debug:
    verbosity: detailed
```

Prints traces and logs to the collector console.

Useful for:

* Learning
* Testing
* Troubleshooting

---

# Sending Test Traces

A sample trace was sent using OTLP HTTP.

```bash
curl -X POST http://localhost:4318/v1/traces
```

The trace successfully flowed through:

```text
curl
  ↓
OTLP Receiver
  ↓
OTEL Collector
  ↓
Batch Processor
  ↓
Debug Exporter
```

---

# Screenshot: Trace Appearing in Collector Logs

Add screenshot here:

```text
screenshots/otel-trace-debug-output.png
```

Expected output:

```text
ResourceSpans
Service Name: my-test-service

Span Name: test-span
Trace ID: 5b8efff798038103d269b633813fc60c
Span ID: eee19b7ec3c1b174
```

This confirmed successful trace ingestion and processing.

---

# Prometheus Alert Rules

## alert-rules.yml

```yaml
groups:
  - name: system-alerts
    rules:

      - alert: HighCPUUsage
        expr: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage detected"

      - alert: HighMemoryUsage
        expr: (1 - node_memory_MemAvailable_bytes /
                node_memory_MemTotal_bytes) * 100 > 85
        for: 2m
        labels:
          severity: warning

      - alert: ContainerDown
        expr: absent(container_last_seen{name="notes-app"})
        for: 1m
        labels:
          severity: critical

      - alert: TargetDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical

      - alert: HighDiskUsage
        expr: (1 - node_filesystem_avail_bytes{mountpoint="/"} /
                node_filesystem_size_bytes{mountpoint="/"}) * 100 > 90
        for: 5m
        labels:
          severity: critical
```

---

# Alert Explanations

## HighCPUUsage

```promql
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
```

Triggers when CPU utilization exceeds 80% for more than 2 minutes.

---

## HighMemoryUsage

```promql
(1 - node_memory_MemAvailable_bytes /
 node_memory_MemTotal_bytes) * 100 > 85
```

Triggers when memory utilization exceeds 85%.

---

## ContainerDown

```promql
absent(container_last_seen{name="notes-app"})
```

Triggers when the notes-app container disappears.

---

## TargetDown

```promql
up == 0
```

Triggers when a Prometheus target becomes unreachable.

---

## HighDiskUsage

```promql
(1 - node_filesystem_avail_bytes{mountpoint="/"} /
 node_filesystem_size_bytes{mountpoint="/"}) * 100 > 90
```

Triggers when root filesystem usage exceeds 90%.

---

# Screenshot: Prometheus Alerts Page

Add screenshot here:

<img width="1919" height="731" alt="image" src="https://github.com/user-attachments/assets/f3548cde-7837-4cb2-8579-861b2500b676" />

```

Expected states:

```text
Inactive
Pending
Firing
```

depending on system conditions.

---

# Grafana Alerting

Grafana was configured to send notifications through Contact Points.

## Contact Point

```text
DevOps Team
```

Notification Type:

```text
Email
```

---

# Custom Grafana Alert Rule

Created:

```text
High Container Memory
```

Query:

```promql
container_memory_usage_bytes{name="notes-app"} / 1024 / 1024
```

Condition:

```text
IS ABOVE 100
```

Evaluation:

```text
Every 1 minute
For 2 minutes
```

Label:

```text
severity=warning
```

---

# Screenshot: Grafana Alert Rule

Add screenshot here:

<img width="1459" height="869" alt="image" src="https://github.com/user-attachments/assets/bcb5bfc0-0e53-40ba-b979-047cb46559f8" />

```

Should show:

* Alert Name
* Query
* Threshold
* Alert State

---

# Full Observability Architecture

The stack now implements all three pillars of observability.

## Metrics Pipeline

```text
[Node Exporter] -----> [Prometheus] -----> [Grafana Dashboards]
[cAdvisor] ----------> [Prometheus] -----> [Grafana Dashboards]
[OTEL Collector] ----> [Prometheus] -----> [Grafana Dashboards]

                                     |
                                     v

                              Alert Rules
                                     |
                                     v

                               Notifications
```

---

## Logs Pipeline

```text
[Docker Containers]
          |
          v
      [Promtail]
          |
          v
        [Loki]
          |
          v
      [Grafana]
```

---

## Traces Pipeline

```text
[curl/App OTLP]
          |
          v

   [OTEL Collector]

          |
          v

    [Debug Exporter]

(Future: Jaeger / Tempo)
```

---

# Complete Architecture Diagram

```text
                    METRICS PIPELINE

[Node Exporter] -----> [Prometheus] -----> [Grafana Dashboards]
[cAdvisor] ----------> [Prometheus] -----> [Grafana Dashboards]
[OTEL Collector] ----> [Prometheus] -----> [Grafana Dashboards]

                                    |
                                    v

                            Alert Rules
                                    |
                                    v

                             Notifications


                     LOGS PIPELINE

[Docker Containers]
          |
          v
      [Promtail]
          |
          v
        [Loki]
          |
          v
      [Grafana]


                    TRACES PIPELINE

[curl/App OTLP]
          |
          v

   [OTEL Collector]

          |
          v

    [Debug Exporter]

(Future: Jaeger / Tempo)
```

---

# Key Takeaways

* Learned OpenTelemetry architecture.
* Understood Receivers, Processors, and Exporters.
* Configured OTLP gRPC and HTTP endpoints.
* Successfully ingested and processed traces.
* Exposed OTEL metrics to Prometheus.
* Created Prometheus alerting rules.
* Configured Grafana alerting and notifications.
* Built a complete observability platform covering Metrics, Logs, and Traces.

The observability stack now includes:

* Prometheus
* Node Exporter
* cAdvisor
* Grafana
* Loki
* Promtail
* OpenTelemetry Collector
* Alerting System

providing a production-style monitoring and observability environment.
