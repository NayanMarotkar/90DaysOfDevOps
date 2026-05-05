# Day 50 – Kubernetes Architecture and Cluster Setup

## Task
You have been building and shipping containers with Docker. But what happens when you need to run hundreds of containers across multiple servers? You need an orchestrator. Today you start your Kubernetes journey — understand the architecture, set up a local cluster, and run your first `kubectl` commands.


---

## Challenge Tasks

### Task 1: Recall the Kubernetes Story
Before touching a terminal, write down from memory:

## 1. Why was Kubernetes created? What problem does it solve that Docker alone cannot?
- Kubernetes was created to manage containers at large scale.
- In large systems, containers need to be restarted, scaled, and monitored automatically.
- Docker alone cannot handle:
  - Auto-scaling
  - Auto-healing
  - Load balancing
  - Multi-node container management
- Docker is used to run containers, while Kubernetes is used to manage them.

## 2. Who created Kubernetes and what was it inspired by?
- Kubernetes was created by Google.
- It was inspired by Google's internal system called Borg.
- Borg was used by Google to manage containers at massive scale.

## 3. What does the name "Kubernetes" mean?
- Kubernetes is a Greek word meaning "Helmsman" or "Ship Pilot".
- It represents controlling and managing containers.

Do not look anything up yet. Write what you remember from the session, then verify against the official docs.

---

### Task 2: Draw the Kubernetes Architecture
From memory, draw or describe the Kubernetes architecture. Your diagram should include:

# Kubernetes Architecture (Simple Notes + Flow)
<img width="1402" height="882" alt="image" src="https://github.com/user-attachments/assets/9cb58e23-cdac-4384-9f10-b706d3be59ad" />

## Architecture Diagram (Text Form)

                [ kubectl ]
                     |
                     v
              [ API Server ]
                     |
    -------------------------------------
    |        |            |             |
    v        v            v             v
 [etcd] [Scheduler] [Controller Manager]
                     |
                     v
              -----------------
              |               |
              v               v
        [ Worker Node 1 ]  [ Worker Node 2 ]

Worker Node Components (each node):
-----------------------------------
- kubelet → talks to API Server, manages pods
- kube-proxy → handles networking between pods
- Container Runtime → runs containers (containerd / CRI-O)

------------------------------------------------------------

## Control Plane (Master Node)
- API Server → entry point (all commands go here)
- etcd → stores cluster data (state)
- Scheduler → decides which node gets the pod
- Controller Manager → ensures desired state = actual state

## Worker Node
- kubelet → runs and manages pods
- kube-proxy → networking (pod-to-pod communication)
- Container Runtime → runs containers

------------------------------------------------------------

## What happens when you run: kubectl apply -f pod.yaml ?

1. kubectl sends request → API Server
2. API Server validates request and stores data in etcd
3. Scheduler checks and selects best Worker Node
4. Controller Manager ensures pod should be created
5. kubelet on selected node gets instruction from API Server
6. kubelet asks Container Runtime to start container
7. kube-proxy sets up networking

👉 Final: Pod is created and running on a Worker Node

------------------------------------------------------------

## What happens if API Server goes down?

- kubectl commands will NOT work
- No new pods can be created
- Existing running pods will continue running
- Cluster becomes unmanaged until API Server is back

------------------------------------------------------------

## What happens if a Worker Node goes down?

- Pods on that node will go down
- Controller Manager detects failure
- Scheduler creates those pods on another healthy node
- System self-heals (auto-healing feature)

------------------------------------------------------------

# Quick Summary
- API Server = brain entry point
- etcd = database
- Scheduler = decision maker
- Controller Manager = ensures correctness
- Worker Nodes = run actual apps

---

### Task 3: Install kubectl
`kubectl` is the CLI tool you will use to talk to your Kubernetes cluster.

Install it:
```bash
# macOS
brew install kubectl

# Linux (amd64)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Windows (with chocolatey)
choco install kubernetes-cli
```

Verify:
```bash
kubectl version --client
```

---

### Task 4: Set Up Your Local Cluster
Choose **one** of the following. Both give you a fully functional Kubernetes cluster on your machine.

**Option A: kind (Kubernetes in Docker)**
```bash
# Install kind
# macOS
brew install kind

# Linux
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Create a cluster
kind create cluster --name devops-cluster

# Verify
kubectl cluster-info
kubectl get nodes
```

**Option B: minikube**
```bash
# Install minikube
# macOS
brew install minikube

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start a cluster
minikube start

# Verify
kubectl cluster-info
kubectl get nodes
```

Write down: Which one did you choose and why?
ans - kind
---

### Task 5: Explore Your Cluster
Now that your cluster is running, explore it:

```bash
# See cluster info
kubectl cluster-info

# List all nodes
kubectl get nodes

# Get detailed info about your node
kubectl describe node <node-name>

# List all namespaces
kubectl get namespaces

# See ALL pods running in the cluster (across all namespaces)
kubectl get pods -A
```

Look at the pods running in the `kube-system` namespace:
```bash
kubectl get pods -n kube-system
```

You should see pods like `etcd`, `kube-apiserver`, `kube-scheduler`, `kube-controller-manager`, `coredns`, and `kube-proxy`. These are the architecture components you drew in Task 2 — running as pods inside the cluster.

**Verify:** Can you match each running pod in `kube-system` to a component in your architecture diagram?

---

### Task 6: Practice Cluster Lifecycle
Build muscle memory with cluster operations:

```bash
# Delete your cluster
kind delete cluster --name devops-cluster
# (or: minikube delete)

# Recreate it
kind create cluster --name devops-cluster
# (or: minikube start)

# Verify it is back
kubectl get nodes
```

Try these useful commands:
```bash
# Check which cluster kubectl is connected to
kubectl config current-context

# List all available contexts (clusters)
kubectl config get-contexts

# See the full kubeconfig
kubectl config view
```

# Kubeconfig (Simple Notes)

## What is a kubeconfig?
- kubeconfig is a configuration file used by kubectl to connect to a Kubernetes cluster.
- It contains:
  - Cluster details (API Server endpoint)
  - User credentials (authentication)
  - Context (which cluster + user to use)

👉 In short: kubeconfig tells kubectl **how to connect and talk to the cluster**

------------------------------------------------------------

## Where is kubeconfig stored?
- Default location:
  ~/.kube/config

👉 This is inside your home directory

Example:
- Linux/Mac → /home/user/.kube/config
- Windows → C:\Users\<username>\.kube\config

------------------------------------------------------------

## Extra Points (Good for Interview)
- You can use multiple clusters using different contexts
- You can change config file using:
  export KUBECONFIG=<path>

------------------------------------------------------------

# Quick Summary
- kubeconfig = connection file for Kubernetes
- Used by kubectl
- Default path = ~/.kube/config
