Day 29 – Introduction to Docker

# Docker Challenge Tasks

## Task 1: What is Docker?

Docker is a containerization platform that allows developers to package applications and their dependencies into containers. These containers can run consistently across different environments such as development, testing, and production.

Docker uses shared operating system resources, which makes it lightweight and efficient. It helps solve problems like *"it works on my machine but not on yours"* by ensuring the application runs the same everywhere.

---

## What is a Container and Why Do We Need Them?

A **container** is a lightweight, portable environment that packages an application along with its dependencies, libraries, and configuration files.

Containers share the **host operating system kernel**, which makes them much lighter and faster than virtual machines.

### Why we need containers
- Consistent environments across different systems
- Faster application deployment
- Efficient use of system resources
- Easy scaling of applications
- Simplified development and testing

---

## Containers vs Virtual Machines

| Feature | Containers | Virtual Machines |
|--------|-----------|-----------------|
| Operating System | Share host OS kernel | Each VM has its own OS |
| Size | Lightweight | Heavy |
| Startup Time | Starts in seconds | Takes minutes |
| Resource Usage | Uses fewer resources | Requires more resources |
| Isolation | Process-level isolation | Full OS-level isolation |

**Summary:**  
Containers are faster and more efficient because they share the host operating system, while virtual machines run a full operating system for each instance.

---

## Docker Architecture

Docker follows a **client-server architecture** and consists of the following main components:

### 1. Docker Client
The Docker client is the command-line interface (CLI) used by users to interact with Docker. Commands like `docker build`, `docker run`, and `docker pull` are sent from the client.

### 2. Docker Daemon
The Docker daemon (`dockerd`) runs in the background and manages Docker objects such as images, containers, networks, and volumes.

### 3. Docker Images
Docker images are **read-only templates** that contain application code, dependencies, libraries, and configuration needed to run an application.

### 4. Docker Containers
A container is a **running instance of a Docker image** where the application actually runs.

### 5. Docker Registry
A Docker registry is a storage location for Docker images. Developers push images to a registry and pull them when needed. A common public registry is **Docker Hub**.

---

## Docker Architecture (Simple Explanation)

Docker works using a client-server model.

1. The **Docker Client** sends commands.
2. The **Docker Daemon** receives those commands and manages Docker resources.
3. Applications are packaged into **Docker Images**.
4. Images are used to create **Containers**.
5. Images can be stored and shared using a **Docker Registry**.

