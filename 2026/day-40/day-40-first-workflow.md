# Day 40 – Your First GitHub Actions Workflow
---

## Challenge Tasks

### Task 1: Set Up
1. Create a new **public** GitHub repository called `github-actions-practice`
2. Clone it locally
3. Create the folder structure: `.github/workflows/`
<img width="1571" height="883" alt="image" src="https://github.com/user-attachments/assets/3be30d19-544f-4f55-854a-20843b0bc001" />

---

### Task 2: Hello Workflow
Create `.github/workflows/hello.yml` with a workflow that:
1. Triggers on every `push`
2. Has one job called `greet`
3. Runs on `ubuntu-latest`
4. Has two steps:
   - Step 1: Check out the code using `actions/checkout`
   - Step 2: Print `Hello from GitHub Actions!`

Push it. Go to the **Actions** tab on GitHub and watch it run.
<img width="1901" height="892" alt="image" src="https://github.com/user-attachments/assets/1b267fb8-0050-429a-b193-f9390f4501d8" />

**Verify:** Is it green? Click into the job and read every step.
Yes,it is green
---

### Task 3: Understand the Anatomy
Look at your workflow file and write in your notes what each key does:
- `on:`
   - Defines `when the worflow is triggered`
   - It listen for event `push`

- `jobs:`
   - Defines the jobs that the worflow will execute
   - A `workflow` can have one or multiple jobs

- `runs-on:`
   - Specifies the virtual machine(runner) env the job will use.
   - `ubuntu-latest`,`windows-latest`,`macos-latest`

- `steps:`
   - Defines the sequences of actions the job will execute
   - Steps run one after another inside the job.

- `uses:`
   - Tells Github to use a prebuilt action
   - Checkout action to clone the repo.

- `run:`
   - Executes commands directly on the runner

- `name:` (on a step)
   - Give the step a humand readable label in the Actions UI.

---

### Task 4: Add More Steps
Update `hello.yml` to also:
1. Print the current date and time
2. Print the name of the branch that triggered the run (hint: GitHub provides this as a variable)
3. List the files in the repo
4. Print the runner's operating system

Push again — watch the new run.
<img width="1897" height="840" alt="image" src="https://github.com/user-attachments/assets/6ec288ec-184f-4583-937b-5489a4e243ea" />

---

### Task 5: Break It On Purpose
1. Add a step that runs a command that will **fail** (e.g., `exit 1` or a misspelled command)
2. Push and observe what happens in the Actions tab
3. Fix it and push again


<img width="1799" height="837" alt="image" src="https://github.com/user-attachments/assets/95d8cb65-3e46-4bc7-9d2c-97a71ea1f699" />
<img width="1826" height="825" alt="image" src="https://github.com/user-attachments/assets/7653b1f2-3a51-497c-b016-1d281bd005af" />

Write in your notes: What does a failed pipeline look like? How do you read the error?

 Failed pipline looks like:
      - Red ❌ in the Actions tab
      - Workflow status: Failed
      - Failed job highlighted in red
   - Read the error
      - Open the failed workflow in Actions
      - Click the failed job
      - Expand the red step
      - Scroll to the bottom
      - Look a few lines above exit code 1 — that’s the real error
---
