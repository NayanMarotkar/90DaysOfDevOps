
# Day 59: Helm - The Package Manager for Kubernetes

## What is Helm?

**Helm** is the package manager for Kubernetes. It helps you define, install, upgrade, and manage Kubernetes applications in a consistent and repeatable way.

Instead of manually writing and applying multiple YAML files, Helm allows you to package all resources into a single **Chart**.

### Three Core Concepts

1. **Chart**  
   A package of pre-configured Kubernetes resources (templates). Like an "app installer".

2. **Release**  
   A specific instance of a chart deployed into a Kubernetes cluster. One chart can have multiple releases.

3. **Repository**  
   A collection of charts (like GitHub for Helm charts). Example: Bitnami repository.

---

## Installation

```bash
# macOS
brew install helm

# Linux
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 && chmod 700 get_helm.sh && ./get_helm.sh

# Verify
helm version
helm env

---

Basic Commands
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm search repo nginx
helm install my-nginx bitnami/nginx
helm list
helm status my-nginx
helm get manifest my-nginx
helm uninstall my-nginx

Customization
1. Using --set

helm install my-nginx bitnami/nginx --set replicaCount=3 --set service.type=NodePort

2. Using values file (-f)
custom-values.yaml (Example):

replicaCount: 3

image:
  repository: nginx
  tag: "1.25"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 250m
    memory: 256Mi

ingress:
  enabled: false

Install using file:

helm install my-app ./my-app -f custom-values.yaml

Upgrade & Rollback

# Upgrade
helm upgrade my-release ./my-app --set replicaCount=5

# History
helm history my-release

# Rollback to previous revision
helm rollback my-release 1

Helm Chart Structure
When you run helm create my-app, you get:

my-app/
├── Chart.yaml              # Chart metadata (name, version, description)
├── values.yaml             # Default configuration values
├── charts/                 # Dependent charts (subcharts)
├── templates/              # Kubernetes manifest templates
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── serviceaccount.yaml
│   └── ...
└── .helmignore

