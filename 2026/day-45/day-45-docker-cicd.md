# Day 45 – Docker Build & Push in GitHub Actions


---

## Challenge Tasks

### Task 1: Prepare
1. Use the app you Dockerized on Day 36 (or any simple Dockerfile)
2. Add the Dockerfile to your `github-actions-practice` repo (or create a minimal one)
3. Make sure `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets are set from Day 44
<img width="1857" height="277" alt="image" src="https://github.com/user-attachments/assets/5290926a-9883-4e9a-a591-519d62771927" />

---

### Task 2: Build the Docker Image in CI
Create `.github/workflows/docker-publish.yml` that:
1. Triggers on push to `main`
2. Checks out the code
3. Builds the Docker image and tags it

**Verify:** Check the build step logs — does the image build successfully?
<img width="1841" height="703" alt="image" src="https://github.com/user-attachments/assets/7a46527c-f25a-4a77-8845-3a2b308ad83a" />

---

### Task 3: Push to Docker Hub
Add steps to:
1. Log in to Docker Hub using your secrets
2. Tag the image as `username/repo:latest` and also `username/repo:sha-<short-commit-hash>`
3. Push both tags

**Verify:** Go to Docker Hub — is your image there with both tags?
<img width="828" height="268" alt="image" src="https://github.com/user-attachments/assets/f480b10b-028d-479e-acd6-ec23daaf4e45" />

---

### Task 4: Only Push on Main
Add a condition so the push step only runs on the `main` branch — not on feature branches or PRs.

Test it: push to a feature branch and verify the image is built but NOT pushed.
<img width="1853" height="847" alt="image" src="https://github.com/user-attachments/assets/6f1c69ce-1f6a-434a-b185-39deaef935d2" />

---

### Task 5: Add a Status Badge
1. Get the badge URL for your `docker-publish` workflow from the Actions tab
2. Add it to your `README.md`
3. Push — the badge should show green

---

### Task 6: Pull and Run It
1. On your local machine (or a cloud server), pull the image you just pushed
2. Run it
3. Confirm it works
<img width="1898" height="1004" alt="Screenshot 2026-04-24 200918" src="https://github.com/user-attachments/assets/affcbde7-068f-4074-9514-f08c6f3328dd" />

Write in your notes: What is the full journey from `git push` to a running container?
What is the full journey from `git push` to a running container?

1. git push – Code is pushed to GitHub.

2. GitHub Actions triggers – The CI/CD workflow starts.

3. Checkout code:

4. Login to Docker Hub: 

5. Build Docker image using the Dockerfile.
    - If code is pushed to main: Docker image is built, tagged, and pushed to Docker Hub.
    - If pushed to other branches or PRs:Docker image is only built for testing.It is not pushed to Docker Hub.

6. Run the container
---

