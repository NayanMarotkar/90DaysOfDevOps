# Day 43 – Jobs, Steps, Env Vars & Conditionals


---

## Challenge Tasks

### Task 1: Multi-Job Workflow
Create `.github/workflows/multi-job.yml` with 3 jobs:
- `build` — prints "Building the app"
- `test` — prints "Running tests"
- `deploy` — prints "Deploying"

Make `test` run only **after** `build` succeeds.
Make `deploy` run only **after** `test` succeeds.

**Verify:** Check the workflow graph in the Actions tab — does it show the dependency chain?
<img width="1842" height="659" alt="image" src="https://github.com/user-attachments/assets/0f12ca35-3b4f-4761-ae06-da5880531fea" />

---

### Task 2: Environment Variables
In a new workflow, use environment variables at 3 levels:
1. **Workflow level** — `APP_NAME: myapp`
2. **Job level** — `ENVIRONMENT: staging`
3. **Step level** — `VERSION: 1.0.0`

Print all three in a single step and verify each is accessible.
<img width="1855" height="634" alt="image" src="https://github.com/user-attachments/assets/8871d840-c322-4244-a51d-ebe19b3dc46f" />

Then use a **GitHub context variable** — print the commit SHA and the actor (who triggered the run).

---

### Task 3: Job Outputs
1. Create a job that **sets an output** — e.g., today's date as a string
2. Create a second job that **reads that output** and prints it
3. Pass the value using `outputs:` and `needs.<job>.outputs.<name>`
<img width="1850" height="538" alt="image" src="https://github.com/user-attachments/assets/67b7fcf3-dd02-4087-ab2b-e02f65ed70d7" />



---

### Task 4: Conditionals
In a workflow, add:
1. A step that only runs when the branch is `main`
2. A step that only runs when the previous step **failed**
3. A job that only runs on **push** events, not on pull requests
4. A step with `continue-on-error: true` — what does this do?
   <img width="1863" height="679" alt="image" src="https://github.com/user-attachments/assets/4eb74e77-0809-4e7e-9c15-9d2b0f16c58e" />


---

### Task 5: Putting It Together
Create `.github/workflows/smart-pipeline.yml` that:
1. Triggers on push to any branch
2. Has a `lint` job and a `test` job running in parallel
3. Has a `summary` job that runs after both, prints whether it's a `main` branch push or a feature branch push, and prints the commit message
<img width="1866" height="709" alt="image" src="https://github.com/user-attachments/assets/764ed494-aa29-4629-8c81-24a53dceb63f" />

