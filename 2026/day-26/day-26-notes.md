Day 26 – GitHub CLI: Manage GitHub from Your Terminal

## What authentication methods does `gh` support?

The GitHub CLI (`gh`) supports multiple authentication methods so users can securely connect their GitHub account.

### Supported Authentication Methods

- **Web Browser Login (OAuth)**  
  The CLI opens a browser where you log in to GitHub and authorize the GitHub CLI.

- **Personal Access Token (PAT)**  
  You can authenticate by entering a GitHub Personal Access Token instead of using the browser.

- **SSH Authentication**  
  If you use SSH keys with GitHub, `gh` can use your SSH key for Git operations.

- **Git Credential Manager**  
  On supported systems, credentials can be stored securely using a credential manager.

✅ These options allow developers to authenticate in different environments such as local machines, servers, or CI/CD pipelines.


## How could you use `gh issue` in a script or automation?

The `gh issue` command from the GitHub CLI can be used in scripts or automation to manage GitHub issues programmatically. This helps automate repetitive tasks and integrate GitHub issue management into CI/CD pipelines.

### Example Use Cases

- **Automatically create an issue when a CI/CD pipeline fails**
```bash
gh issue create --title "CI Pipeline Failed" --body "The latest build failed. Please check the logs."

## 1. What merge methods does `gh pr merge` support?

The `gh pr merge` command supports three merge methods:

- **Merge Commit (`--merge`)**  
  Combines all commits from the pull request into the main branch with a merge commit.

- **Squash Merge (`--squash`)**  
  Combines all commits from the pull request into **one single commit** before merging.

- **Rebase Merge (`--rebase`)**  
  Re-applies the pull request commits on top of the target branch without creating a merge commit.

---

## 2. How would you review someone else's PR using `gh`?

You can review a pull request using the GitHub CLI with these steps:

1. **View the list of pull requests**
```bash
gh pr list

## How could `gh run` and `gh workflow` be useful in a CI/CD pipeline?

The `gh run` and `gh workflow` commands from GitHub CLI help developers and DevOps engineers manage **GitHub Actions workflows** directly from the terminal. They are useful for monitoring, triggering, and controlling CI/CD pipelines.

### Using `gh run`

`gh run` is used to manage and monitor workflow runs.

**Example uses:**

- **List workflow runs**
```bash
gh run list

