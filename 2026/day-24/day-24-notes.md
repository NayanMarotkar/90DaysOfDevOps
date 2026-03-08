Day 24 – Advanced Git: Merge, Rebase, Stash & Cherry Pick

## Fast-Forward Merge
A **fast-forward merge** happens when the main branch has not changed since the new branch was created.

Git simply moves the main branch pointer forward to the latest commit of the feature branch.  
No extra merge commit is created.

Example:
A---B---C (main)  
         \
          D---E (feature)

After merge:

A---B---C---D---E (main)

---

## When Git Creates a Merge Commit
Git creates a **merge commit** when both branches have new commits that the other branch does not have.

Since the histories are different, Git combines them and creates a new commit called a **merge commit**.

Example:
A---B---C (main)  
     \  
      D---E (feature)

After merge:

A---B---C-------M (main)  
     \         /  
      D---E---  

`M` is the merge commit.

---

## Merge Conflict
A **merge conflict** happens when Git cannot automatically merge changes from two branches.

This usually happens when the **same line of the same file was changed in both branches**.

Git will stop the merge and ask you to manually choose which changes to keep or combine them.

Steps to fix:
1. Open the file with the conflict.
3. Edit and decide which code should stay.
4. Save the file.
5. Add and commit the resolved file.

## What Rebase Does
**Rebase** takes your commits from one branch and **reapplies them on top of another branch**.  

It’s like “moving” your work to start from the latest commit of the main branch.

---

## How History is Different from Merge
- **Merge:** keeps all commits and shows a branch structure with a merge commit.
- **Rebase:** rewrites commits so history looks **linear**, as if all work was done sequentially.

---

## Why You Should Never Rebase Shared Commits
Rebasing **rewrites commit history**.  
If someone else already pulled your old commits, rebasing will create **conflicting histories** and force everyone to fix them.  

Rule of thumb: **Only rebase local/private commits.**

---

## When to Use Rebase vs Merge
- **Rebase:**  
  - Keeps history clean and linear.  
  - Good for updating your branch with the latest main branch changes before merging.  

- **Merge:**  
  - Keeps the full history of work and branch structure.  
  - Safer for shared branches and when you want to preserve the context of parallel work.
 
## Squash Merging
**Squash merge** takes all the commits from a feature branch and **combines them into a single commit** when merging into the main branch.

Example:  
Feature branch commits:  
D---E---F
After squash merge into main:  
main: A---B---C---G
`G` contains all the changes from `D`, `E`, and `F` as **one commit**.

---

## When to Use Squash Merge vs Regular Merge
- **Squash merge:**  
  - Use when you want to **keep main branch history clean and simple**.  
  - Good for small features, experiments, or when feature branch had many tiny/fix commits.  

- **Regular merge:**  
  - Use when you want to **preserve the full commit history** of the feature branch.  
  - Good for big features where the sequence of commits is important.

---

## Trade-Off of Squashing
- ✅ Keeps history clean and linear.  
- ❌ Loses individual commits and their messages from the feature branch.  
- ❌ Harder to see **step-by-step progress** in the feature branch after merge.

  ## Difference Between `git stash pop` and `git stash apply`

- **`git stash apply`**  
  - Applies the changes from the stash to your working directory.  
  - **Keeps the stash** in the stash list so you can reuse it later.  

- **`git stash pop`**  
  - Applies the changes from the stash **and removes it** from the stash list.  
  - Handy when you want to apply the stash **just once**.

---

## When to Use `git stash` in Real-World Workflow

- When you are working on a feature but need to **quickly switch branches** without committing incomplete work.  
- When you want to **save your current changes temporarily** before pulling updates or resolving conflicts.  
- Example workflow:
  1. `git stash` → save changes.
  2. `git checkout main` → switch branch to fix a bug.
  3. `git pull` → update main branch.
  4. `git checkout feature` → go back to your feature branch.
  5. `git stash pop` → reapply your saved changes.

 ## Git Cherry-Pick
**`git cherry-pick <commit>`** takes a specific commit from one branch and **applies it to your current branch** as a new commit.  

It’s like copying a single change without merging the whole branch.

---

## When to Use Cherry-Pick
- When you need a **specific bug fix or feature** from another branch without merging the entire branch.  
- Example:  
  - A hotfix was committed to `main`  
  - You want the same fix on `feature-signup` branch:  
    ```bash
    git checkout feature-signup
    git cherry-pick <commit-hash>
    ```

---

## What Can Go Wrong
- **Merge conflicts:** if the same lines were changed in your branch, you’ll need to resolve them manually.  
- **Duplicate commits:** if the same change eventually gets merged, you might have **duplicate commits** in history.  
- **Messy history:** frequent cherry-picking can make history harder to follow, especially in big teams.
