# Day 42 – Runners: GitHub-Hosted & Self-Hosted

## Task
---

## Challenge Tasks

### Task 1: GitHub-Hosted Runners
1. Create a workflow with 3 jobs, each on a different OS:
   - `ubuntu-latest`
   - `windows-latest`
   - `macos-latest`
2. In each job, print:
   - The OS name
   - The runner's hostname
   - The current user running the job
3. Watch all 3 run in parallel
<img width="1855" height="777" alt="image" src="https://github.com/user-attachments/assets/947f0e78-e76d-438f-bd4b-017a2dec88ad" />

Write in your notes: What is a GitHub-hosted runner? Who manages it?
A GitHub-hosted runner is a temporary virtual machine provided and managed by GitHub to run your workflow jobs automatically.

---

### Task 2: Explore What's Pre-installed
1. On the `ubuntu-latest` runner, run a step that prints:
   - Docker version
   - Python version
   - Node version
   - Git version
2. Look up the GitHub docs for the full list of pre-installed software on `ubuntu-latest`
<img width="1875" height="815" alt="image" src="https://github.com/user-attachments/assets/e9ded52d-8871-43a0-8676-3054fa6fdc5b" />

Write in your notes: Why does it matter that runners come with tools pre-installed?
It matters because runners come with tools pre-installed, so you don’t need to install them manually and your workflows run faster and more easily.

---

### Task 3: Set Up a Self-Hosted Runner
1. Go to your GitHub repo → Settings → Actions → Runners → **New self-hosted runner**
2. Choose Linux as the OS
3. Follow the instructions to download and configure the runner on:
   - Your local machine, OR
   - A cloud VM (EC2, Utho, or any VPS)
4. Start the runner — verify it shows as **Idle** in GitHub

**Verify:** Your runner appears in the Runners list with a green dot.
<img width="1810" height="945" alt="image" src="https://github.com/user-attachments/assets/4888af4d-38c9-44cf-aae5-96b40f69f22f" />
<img width="1343" height="489" alt="image" src="https://github.com/user-attachments/assets/7bc012c2-e8e5-456e-823f-6b8b2c897ccc" />

---

### Task 4: Use Your Self-Hosted Runner
1. Create `.github/workflows/self-hosted.yml`
2. Set `runs-on: self-hosted`
3. Add steps that:
   - Print the hostname of the machine (it should be YOUR machine/VM)
   - Print the working directory
   - Create a file and verify it exists on your machine after the run
4. Trigger it and watch it run on your own hardware

**Verify:** Check your machine — is the file there?

---

### Task 5: Labels
1. Add a **label** to your self-hosted runner (e.g., `my-linux-runner`)
2. Update your workflow to use `runs-on: [self-hosted, my-linux-runner]`
3. Trigger it — does it still pick up the job?
<img width="1311" height="222" alt="image" src="https://github.com/user-attachments/assets/59702be4-cbd4-48b0-8738-08b03b6078cd" />

Write in your notes: Why are labels useful when you have multiple self-hosted runners?
Labels are useful because they let you choose the correct self-hosted runner (like OS, region, or tools) when you have multiple runners.
---

### Task 6: GitHub-Hosted vs Self-Hosted
Fill this in your notes:

| | GitHub-Hosted | Self-Hosted |
|---|---|---|
| Who manages it? | GitHub | You / Your team |
| Cost | Free (limited) / Pay for usage | You pay for your own server |
| Pre-installed tools | Yes (Docker, Node, Java, etc.) | You install and manage |
| Good for | Quick setup, simple CI/CD | Custom setup, deployments, private infra |
| Security concern | Code runs on GitHub machines | Full control but must secure yourself |

---


