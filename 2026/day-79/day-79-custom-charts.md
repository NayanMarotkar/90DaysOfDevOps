# Day 79 - Creating a Custom Helm Chart for AI-BankApp

## Overview

Today I converted the AI-BankApp Kubernetes manifests into a reusable Helm Chart. Instead of deploying 12 separate YAML files manually, the complete application stack can now be deployed using a single Helm command.

The application consists of:

* Spring Boot AI-BankApp
* MySQL Database
* Ollama AI Chatbot
* ConfigMaps and Secrets
* Persistent Storage
* Horizontal Pod Autoscaler (HPA)

---

# Why Helm?

Managing multiple Kubernetes YAML files becomes difficult as applications grow.

### Before Helm

```bash
kubectl apply -f namespace.yml
kubectl apply -f configmap.yml
kubectl apply -f secrets.yml
kubectl apply -f pvc.yml
kubectl apply -f mysql-deployment.yml
kubectl apply -f ollama-deployment.yml
kubectl apply -f bankapp-deployment.yml
kubectl apply -f service.yml
kubectl apply -f hpa.yml
```

### After Helm

```bash
helm install my-bankapp bankapp/
```

A single command deploys the entire stack.

---

# Side-by-Side Comparison

## Example 1: ConfigMap

### Raw Kubernetes Manifest

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: bankapp-config
data:
  MYSQL_HOST: mysql
  MYSQL_PORT: "3306"
  MYSQL_DATABASE: bankappdb
```

### Helm Template

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "bankapp.fullname" . }}-config
data:
  MYSQL_HOST: {{ include "bankapp.fullname" . }}-mysql
  MYSQL_PORT: "3306"
  MYSQL_DATABASE: {{ .Values.config.mysqlDatabase | quote }}
```

### Benefit

Database configuration is now configurable through values.yaml instead of hardcoded values.

---

## Example 2: Secret

### Raw Kubernetes Manifest

```yaml
apiVersion: v1
kind: Secret
data:
  MYSQL_ROOT_PASSWORD: VGVzdEAxMjM=
```

### Helm Template

```yaml
apiVersion: v1
kind: Secret
data:
  MYSQL_ROOT_PASSWORD: {{ .Values.secrets.mysqlRootPassword | b64enc | quote }}
```

### Benefit

No manual Base64 encoding required.

---

## Example 3: Deployment Image

### Raw Kubernetes Manifest

```yaml
image: trainwithshubham/ai-bankapp-eks:latest
```

### Helm Template

```yaml
image: "{{ .Values.bankapp.image.repository }}:{{ .Values.bankapp.image.tag }}"
```

### Benefit

Image tags can be changed without modifying templates.

---

# Complete values.yaml

```yaml
bankapp:
  replicaCount: 4
  image:
    repository: trainwithshubham/ai-bankapp-eks
    tag: "latest"
    pullPolicy: Always

  resources:
    requests:
      memory: "256Mi"
      cpu: "250m"
    limits:
      memory: "512Mi"
      cpu: "500m"

  service:
    type: NodePort
    port: 8080

  autoscaling:
    enabled: true
    minReplicas: 2
    maxReplicas: 4
    targetCPUUtilization: 70

mysql:
  enabled: true
  image:
    repository: mysql
    tag: "8.0"

  persistence:
    size: 5Gi
    storageClass: standard

ollama:
  enabled: true
  image:
    repository: ollama/ollama
    tag: latest

  model: tinyllama

  persistence:
    size: 10Gi
    storageClass: standard

config:
  mysqlDatabase: bankappdb
  ollamaUrl: ""

secrets:
  mysqlRootPassword: Test@123
  mysqlUser: root
  mysqlPassword: Test@123

storageClass:
  create: false
  name: gp3

gateway:
  enabled: false

httpRoute:
  enabled: false

ingress:
  enabled: false
```

---

# values.yaml Explanation

| Section      | Purpose                          |
| ------------ | -------------------------------- |
| bankapp      | Spring Boot application settings |
| mysql        | MySQL deployment settings        |
| ollama       | AI chatbot settings              |
| config       | Shared application configuration |
| secrets      | Database credentials             |
| storageClass | Persistent storage configuration |
| gateway      | Envoy Gateway support            |
| ingress      | Ingress configuration            |
| httpRoute    | Gateway API configuration        |

---

# Helm Go Template Cheat Sheet

## Access Values

```yaml
{{ .Values.bankapp.replicaCount }}
```

---

## if Condition

```yaml
{{- if .Values.ollama.enabled }}
...
{{- end }}
```

---

## range Loop

```yaml
{{- range .Values.list }}
...
{{- end }}
```

---

## with Block

```yaml
{{- with .Values.bankapp.resources }}
resources:
{{ toYaml . | nindent 2 }}
{{- end }}
```

---

## include

```yaml
{{ include "bankapp.fullname" . }}
```

Used to call helper templates.

---

## toYaml

```yaml
{{ toYaml .Values.resources }}
```

Converts objects into valid YAML.

---

## nindent

```yaml
{{ toYaml . | nindent 8 }}
```

Adds proper indentation.

---

## b64enc

```yaml
{{ .Values.secrets.mysqlPassword | b64enc }}
```

Encodes values as Base64.

---

# Helm Validation

## Lint Chart

```bash
helm lint bankapp/
```

Output:

```text
==> Linting bankapp/

[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

---

## Render Templates

```bash
helm template my-bankapp bankapp/
```

Example Output:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-bankapp-service

spec:
  type: NodePort

  ports:
  - port: 8080
    targetPort: 8080

  selector:
    app: my-bankapp
```

All template variables were successfully rendered.

---

# Deployment

```bash
helm install my-bankapp bankapp \
  -n bankapp \
  --create-namespace \
  --set storageClass.create=false \
  --set mysql.persistence.storageClass=standard \
  --set ollama.persistence.storageClass=standard
```

---

# Verification

```bash
helm list -n bankapp
```

```bash
kubectl get all -n bankapp
```

Output:

```text
deployment.apps/my-bankapp
deployment.apps/my-bankapp-mysql
deployment.apps/my-bankapp-ollama

service/my-bankapp-service
service/my-bankapp-mysql
service/my-bankapp-ollama

horizontalpodautoscaler/my-bankapp-hpa
```

---

# Testing Application

Port Forward:

```bash
kubectl port-forward svc/my-bankapp-service \
  -n bankapp \
  8080:8080
```

Access:

```text
http://localhost:8080/login
```

Application successfully redirected to the Spring Security login page.

---

# Disabling Ollama

Helm allows optional components to be disabled.

Deploy without Ollama:

```bash
helm install my-bankapp bankapp \
  --set ollama.enabled=false
```

Resources removed automatically:

* Ollama Deployment
* Ollama Service
* Ollama PVC
* Ollama Init Container

This demonstrates how a single value controls an entire application component.

---

# Screenshot

Insert screenshot here showing:

* `kubectl get all -n bankapp`
  <img width="1535" height="608" alt="image" src="https://github.com/user-attachments/assets/b99fd1e9-2073-4d5f-8839-f23cb7f528ec" />

* Successful Helm deployment
<img width="1541" height="444" alt="image" src="https://github.com/user-attachments/assets/6a9a7de0-41f9-4253-8d79-f67373f413d5" />

* AI-BankApp login page running through Helm on Kind
<img width="1901" height="921" alt="image" src="https://github.com/user-attachments/assets/820996d1-ea86-4352-b187-ed4dfa20dd5b" />

---

# Key Learnings

* Helm transforms static Kubernetes YAML into reusable templates.
* values.yaml centralizes configuration management.
* Secrets can be dynamically encoded using b64enc.
* Optional components can be enabled or disabled using conditional templates.
* Helm simplifies deployment, upgrades, rollbacks, and environment customization.
* A complete AI application stack can be deployed using a single Helm command.

# Day 79 Complete ✅

Successfully built and deployed a custom Helm chart for AI-BankApp, including Spring Boot, MySQL, Ollama AI, PVCs, ConfigMaps, Secrets, Services, and HPA support.
