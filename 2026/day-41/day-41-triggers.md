# Day 41 – Triggers & Matrix Builds

---

## Challenge Tasks

### Task 1: Trigger on Pull Request
1. Create `.github/workflows/pr-check.yml`
2. Trigger it only when a pull request is **opened or updated** against `main`
3. Add a step that prints: `PR check running for branch: <branch name>`
4. Create a new branch, push a commit, and open a PR
   <img width="1898" height="825" alt="image" src="https://github.com/user-attachments/assets/081f43a5-339d-439f-a604-9499f134ee0c" />

6. Watch the workflow run automatically
**Verify:** Does it show up on the PR page?
Yes,it show up on the PR page
<img width="1663" height="856" alt="image" src="https://github.com/user-attachments/assets/24c6449c-489d-4d8a-82dd-d2a3f736b9df" />
<img width="1890" height="797" alt="image" src="https://github.com/user-attachments/assets/b7aa0dcc-f518-4f0a-8460-5a35bd710b8b" />


---

### Task 2: Scheduled Trigger
1. Add a `schedule:` trigger to any workflow using cron syntax
2. Set it to run every day at midnight UTC
   <img width="1653" height="815" alt="image" src="https://github.com/user-attachments/assets/5c9385c8-379e-4d24-ad65-2cea45b808d7" />

4. Write in your notes: What is the cron expression for every Monday at 9 AM?
   cron expression for every Monday at 9 AM is 0 9 * * 1

---

### Task 3: Manual Trigger
1. Create `.github/workflows/manual.yml` with a `workflow_dispatch:` trigger
2. Add an **input** that asks for an `environment` name (staging/production)
3. Print the input value in a step
4. Go to the **Actions** tab → find the workflow → click **Run workflow**

**Verify:** Can you trigger it manually and see your input printed?
<img width="1880" height="862" alt="image" src="https://github.com/user-attachments/assets/2ce2986c-5b89-4b1a-a50f-ada1c84e7b79" />
<img width="1877" height="701" alt="image" src="https://github.com/user-attachments/assets/2d298c5c-d11c-44b9-b43e-66640d51bfa7" />


---

### Task 4: Matrix Builds
Create `.github/workflows/matrix.yml` that:
1. Uses a matrix strategy to run the same job across:
   - Python versions: `3.10`, `3.11`, `3.12`
2. Each job installs Python and prints the version
3. Watch all 3 run in parallel
<img width="1844" height="879" alt="image" src="https://github.com/user-attachments/assets/0d1ec0a6-4002-409d-b2a1-dcb78bed29b4" />
<img width="1858" height="695" alt="image" src="https://github.com/user-attachments/assets/296dd4ea-21ab-4bdb-bec0-06c6018d8d35" />
<img width="1862" height="678" alt="image" src="https://github.com/user-attachments/assets/39b61c38-5ed2-4c79-9c0c-c3768f684c56" />

Then extend the matrix to also include 2 operating systems — how many total jobs run now?
<img width="1890" height="869" alt="image" src="https://github.com/user-attachments/assets/df4f49e0-a7ed-4cb2-8d68-915677fc8cbf" />


---

### Task 5: Exclude & Fail-Fast
1. In your matrix, **exclude** one specific combination (e.g., Python 3.10 on Windows)
2. Set `fail-fast: false` — trigger a failure in one job and observe what happens to the rest
<img width="1852" height="801" alt="image" src="https://github.com/user-attachments/assets/e1d05748-a31c-4e54-9069-b07311d5757f" />

3. Write in your notes: What does `fail-fast: true` (the default) do vs `false`?

fail-fast: true (default): If one job fails, the remaining matrix jobs are cancelled.
fail-fast: false: If one job fails, the other jobs continue running until completion.

---

