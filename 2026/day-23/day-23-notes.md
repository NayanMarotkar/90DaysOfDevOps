Day 23 – Git Branching & Working with GitHub

# Task 1: Understanding Branches

## 1. What is a branch in Git?

A branch in Git is a separate line of development that allows developers to work on new features or fixes without affecting the main branch.

---

## 2. Why do we use branches instead of committing everything to main?

Branches allow developers to work on features, bug fixes, or experiments safely without breaking the main branch. Once the work is tested, it can be merged into the main branch.

---

## 3. What is HEAD in Git?

HEAD in Git is a pointer that refers to the current branch and the latest commit you are working on.

---

## 4. What happens to your files when you switch branches?

When you switch branches, Git updates the files in your working directory to match the selected branch. Uncommitted changes may remain if they do not conflict, otherwise Git will prevent the switch.

## 5. What is the difference between origin and upstream in Git?

In Git, **origin** and **upstream** are names used for remote repositories.

- **origin**  
  Origin is the default name for the remote repository that you cloned from. It usually refers to your own copy of the repository on a platform like GitHub.

- **upstream**  
  Upstream refers to the original repository from which a fork was created. It is used to fetch updates from the main project repository.

### Example

If you fork a repository on GitHub:

- **origin** → your forked repository  
- **upstream** → the original repository you forked from

This setup allows you to pull updates from the original repository while pushing your changes to your own fork.

## 6. What is the difference between git fetch and git pull?

Both `git fetch` and `git pull` are used to get updates from a remote repository, but they work differently.

### git fetch
`git fetch` downloads the latest changes from the remote repository but does not merge them into your current branch. It only updates the remote tracking branches so you can review the changes before merging.

### git pull
`git pull` downloads the latest changes from the remote repository and automatically merges them into your current branch.

### Simple Difference

- **git fetch** → Download changes only  
- **git pull** → Download changes + Merge them into your branch

## 7. What is the difference between clone and fork?

### Fork
A fork is a copy of someone else's repository that is created in your own GitHub account. It allows you to make changes to the project without affecting the original repository.

### Clone
A clone is a copy of a repository that is downloaded from a remote repository (such as GitHub) to your local computer so you can work on it.

### Key Difference

- **Fork** → Creates a copy of a repository in your GitHub account.
- **Clone** → Downloads a repository from GitHub to your local machine.

## 8. When would you clone vs fork?

### When to use Fork
You use **fork** when you want to contribute to someone else's project but do not have direct access to the original repository.

### When to use Clone
You use **clone** when you want to download a repository to your local machine to start working on it.

### Example

- **Fork** → Copy the project to your GitHub account.
- **Clone** → Download the project to your computer.

## 9. After forking, how do you keep your fork in sync with the original repository?

To keep your fork updated with the original repository, you need to connect it to the original repository using **upstream**.

### Steps

1. Add the original repository as upstream

```bash
git remote add upstream <original-repository-url>

