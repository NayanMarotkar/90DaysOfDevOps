Day 25 – Git Reset vs Revert & Branching Strategies

# Task 1: Git Reset — Hands-On

## Steps Performed
1. Made 3 commits in practice repo: **A**, **B**, **C**.  
2. Used `git reset --soft HEAD~1` to go back one commit.  
   - **Observation:** The last commit (**C**) was removed from history, but its changes remained **staged** in the index.  
   - I was able to **re-commit immediately** without re-adding files.  

3. Re-committed, then used `git reset --mixed HEAD~1`.  
   - **Observation:** The last commit was removed, changes remained in the **working directory** but were **unstaged**.  
   - I had to `git add` again before re-committing.  

4. Re-committed, then used `git reset --hard HEAD~1`.  
   - **Observation:** The last commit was removed, and all changes from that commit were **completely lost** from both the index and working directory.  

---

## Difference Between `--soft`, `--mixed`, and `--hard`

| Option       | HEAD Moves | Staging Area | Working Directory | Notes |
|-------------|------------|-------------|-----------------|-------|
| `--soft`    | Yes        | Kept        | Kept            | Undo commit but keep changes staged |
| `--mixed`   | Yes        | Cleared     | Kept            | Undo commit, unstage changes |
| `--hard`    | Yes        | Cleared     | Cleared         | Undo commit and discard all changes |

---

## Destructiveness
- **`--hard`** is **destructive** because it **deletes changes** in the working directory and staging area permanently.  
- `--soft` and `--mixed` are non-destructive (changes remain in index or working directory).

---

## When to Use Each
- `--soft`: Fix or reword last commit without losing staged changes.  
- `--mixed` (default): Undo commit and unstage changes for adjustments.  
- `--hard`: Discard last commit and all changes — useful for cleaning up experimental work.

---

## Caution with Pushed Commits
- **Never use `git reset` on commits that are already pushed** to a shared branch.  
- It rewrites history and can cause conflicts for other collaborators. Use `git revert` instead for safely undoing commits in shared repositories.

# Git Revert vs Git Reset

## 1. How is `git revert` different from `git reset`?

- **`git revert`**  
  - Creates a **new commit** that undoes the changes introduced by a previous commit.  
  - Preserves the commit history; no commits are removed.

- **`git reset`**  
  - Moves the branch pointer to a previous commit, effectively **removing commits** from the branch.  
  - Alters the commit history; changes may be lost if not backed up.

---

## 2. Why is `revert` considered safer than `reset` for shared branches?

- `git revert` **does not delete history**, so other team members can safely pull and continue working.  
- `git reset` **rewrites history**, which can cause conflicts or lost work if others have based their work on commits you reset.  
- Therefore, `revert` is preferred on **shared/public branches**, while `reset` is more suited for **local/private branches**.

---

## 3. When would you use `revert` vs `reset`?

- **Use `git revert` when:**  
  - Working on a **shared branch**.  
  - You want to **undo a commit safely** without rewriting history.

- **Use `git reset` when:**  
  - Working on a **private or local branch**.  
  - You want to **completely remove commits** before sharing.  
  - Cleaning up mistakes or reorganizing your local commits.
 
  # Git Reset vs Git Revert — Summary

| Feature | `git reset` | `git revert` |
|---------|-------------|--------------|
| **What it does** | Moves the branch pointer to a previous commit, effectively **removing commits** from the branch | Creates a **new commit** that undoes the changes of a previous commit |
| **Removes commit from history?** | ✅ Yes, commits are removed from the branch history | ❌ No, history is preserved; a new commit is added |
| **Safe for shared/pushed branches?** | ❌ No, rewriting history can cause conflicts for others | ✅ Yes, preserves history, safe for shared branches |
| **When to use** | On **local/private branches** to clean up or reorganize commits | On **shared/public branches** to safely undo a commit without affecting history |

## Git Strategy for Different Scenarios

### 1. Which strategy would you use for a startup shipping fast?

- **`git revert`**  
  - For a startup that ships fast and often, a simple workflow with **feature branches and quick fixes** works best.  
  - Reverting mistakes by creating new commits helps keep all changes transparent and avoids rewriting history that others might depend on. :contentReference[oaicite:0]{index=0}

**➡ Recommended:** `git revert`  
- Keeps history intact  
- Safe for frequent pushes  
- Easy for others to follow

---

### 2. Which strategy would you use for a large team with scheduled releases?

- **`git revert`** is typically preferred for large teams with structured releases because it **preserves history** and avoids force‑pushes that can disrupt others’ work.  
- Larger teams often have protected main/release branches and a longer review cycle, so retaining a clear commit history is valuable. :contentReference[oaicite:1]{index=1}

**➡ Recommended:** `git revert`  
- Safe for shared branches  
- Works well with scheduled release workflows

---

### 3. Which one does your favorite open‑source project use? (Check any repo on GitHub)

Most **well‑known open‑source projects** (e.g., the *Linux kernel*, large libraries, frameworks) avoid rewriting shared history and rely on **git revert** (or merge‑based workflows) when undoing public commits rather than using `git reset` on shared branches.  
- This is because **revert preserves commit history and collaboration integrity**, especially in distributed projects with many contributors. :contentReference[oaicite:2]{index=2}

**➡ Common practice in open‑source:** `git revert`
- Rarely resets publicly pushed commits
- Keeps historical traceability of code changes
