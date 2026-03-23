# Day 39 – What is CI/CD?

## Objective

Today’s goal is to **understand CI/CD concepts** before writing any pipelines.  
Focus: why CI/CD exists, what problems it solves, and the anatomy of a pipeline.

---

# Task 1 – The Problem

Scenario: 5 developers manually pushing code to production.

**Notes:**

1. **What can go wrong?**
   - Conflicting code changes
   - Bugs introduced in production
   - Environment differences between dev and prod
   - Human errors in manual deployment

2. **"It works on my machine"**
   - Local environment differs from staging/production
   - Causes integration problems and unexpected failures

3. **Manual deployment frequency**
   - Safe: 1–2 times/day for small teams
   - Frequent manual deploys increase risk

---

# Task 2 – CI vs CD

### 1️⃣ Continuous Integration (CI)
- Developers merge code frequently into a shared repo.
- Automated builds and tests run on every merge.
- **Example:** React app runs unit tests automatically after each push.

### 2️⃣ Continuous Delivery (CD)
- Ensures code is **always deployable**.
- Automates build, test, and artifact preparation for deployment.
- **Example:** FastAPI service builds Docker images and deploys to staging automatically.

### 3️⃣ Continuous Deployment
- Every successful change is automatically deployed to production.
- No manual approval needed.
- **Example:** E-commerce frontend updates live after every merge to main.

---

# Task 3 – Pipeline Anatomy

| Component  | Description |
|------------|-------------|
| Trigger    | Event that starts the pipeline (`push`, `PR merge`, `cron`) |
| Stage      | Logical phase (`build`, `test`, `deploy`) |
| Job        | Unit of work inside a stage (`run tests`, `build Docker image`) |
| Step       | Single command/action inside a job (`npm install`, `pytest`) |
| Runner     | Machine executing the job (GitHub-hosted or self-hosted) |
| Artifact   | Output produced by a job (Docker image, binary, logs) |

---

# Task 4 – CI/CD Pipeline Diagram

### Scenario:
> Developer pushes code → App is tested → Docker image is built → Deployed to staging

### ASCII Hand-Drawn Pipeline

```
+------------------+
|  Developer Push  |
+------------------+
          │
          ▼
    +-------------+
    |  Build      |
    | - Install   |
    | - Compile   |
    +-------------+
          │
          ▼
    +-------------+
    |  Test       |
    | - Unit      |
    | - Integration |
    +-------------+
          │
          ▼
    +------------------+
    | Deploy Stage     |
    | - Build Docker   |
    | - Push to Registry|
    | - Staging Deploy |
    +------------------+
```

---

# Task 5 – Explore in the Wild

Example: **Kubernetes GitHub repo** → `.github/workflows/`

- **Trigger:** Push to main branch
- **Jobs:** 2 jobs (build + test)
- **What it does:** Builds Docker images, runs unit/e2e tests, optionally deploys to staging

**Notes:**
- Triggers include `push`, `pull_request`, or `cron`
- Jobs run isolated and in parallel
- Artifacts can be used by downstream jobs

---

# Key Learnings

1. CI/CD is a **practice**, not just a tool.
2. Automation reduces **manual errors** and ensures consistency.
3. Pipelines have **stages, jobs, steps, triggers, runners, and artifacts**.
4. CI catches integration issues early, Delivery ensures deployable code, Deployment pushes automatically to production.

---
