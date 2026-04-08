# Day 44 – Secrets, Artifacts & Running Real Tests in CI

## Task

---

## Challenge Tasks

### Task 1: GitHub Secrets
1. Go to your repo → Settings → Secrets and Variables → Actions
2. Create a secret called `MY_SECRET_MESSAGE`
3. Create a workflow that reads it and prints: `The secret is set: true` (never print the actual value)
4. Try to print `${{ secrets.MY_SECRET_MESSAGE }}` directly — what does GitHub show?
<img width="1881" height="802" alt="Screenshot 2026-04-08 051502" src="https://github.com/user-attachments/assets/da5958e2-ad0e-4b34-b997-a92e82eaa768" />

Write in your notes: Why should you never print secrets in CI logs?
Never print secrets in CI logs because logs are visible, stored, and can expose sensitive tokens or passwords to anyone, leading to security breaches
---

### Task 2: Use Secrets as Environment Variables
1. Pass a secret to a step as an environment variable
2. Use it in a shell command without ever hardcoding it
3. Add `DOCKER_USERNAME` and `DOCKER_TOKEN` as secrets (you'll need these on Day 45)
<img width="1860" height="871" alt="image" src="https://github.com/user-attachments/assets/1593f41d-6f34-4abd-8a06-4a09a0c4beed" />

---

### Task 3: Upload Artifacts
1. Create a step that generates a file — e.g., a test report or a log file
2. Use `actions/upload-artifact` to save it
3. After the workflow runs, download the artifact from the Actions tab
<img width="1833" height="783" alt="image" src="https://github.com/user-attachments/assets/5c222eab-8f56-4201-aa20-aefd46187736" />

**Verify:** Can you see and download it from GitHub?

---

### Task 4: Download Artifacts Between Jobs
1. Job 1: generate a file and upload it as an artifact
2. Job 2: download the artifact from Job 1 and use it (print its contents)
<img width="1833" height="783" alt="image" src="https://github.com/user-attachments/assets/c00b1d83-0651-4463-ac91-0fc8aab20111" />
<img width="1831" height="706" alt="image" src="https://github.com/user-attachments/assets/37112524-4427-469a-b7f4-8c2922d6ca44" />

Write in your notes: When would you use artifacts in a real pipeline?
Artifacts are used to store and transfer files (like build outputs, test reports, or binaries) between jobs in a CI/CD pipeline

---

### Task 5: Run Real Tests in CI
Take any script from your earlier days (Python or Shell) and run it in CI:
1. Add your script to the `github-actions-practice` repo
2. Write a workflow that:
   - Checks out the code
   - Installs any dependencies needed
   - Runs the script
   - Fails the pipeline if the script exits with a non-zero code
3. Intentionally break the script — verify the pipeline goes red
4. Fix it — verify it goes green again
<img width="1860" height="826" alt="image" src="https://github.com/user-attachments/assets/5d215c26-de07-48fe-a5eb-58e44b27bb82" />

---

### Task 6: Caching
1. Add `actions/cache` to a workflow that installs dependencies
2. Run it twice — observe the time difference
3. Write in your notes: What is being cached and where is it stored?
   In CI/CD pipelines, dependencies or build outputs are cached and stored in the CI platform’s cache storage (e.g., GitHub Actions cache) to speed up future runs
<img width="1847" height="690" alt="image" src="https://github.com/user-attachments/assets/8cb5648b-695c-43f4-aae6-85bb291a8bb0" />

---

