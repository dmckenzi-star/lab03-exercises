# Lab 03: Git and GitHub

This repository documents my practice with local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization

```text
ls -la
total 12
drwxr-xr-x 3 mac mac 4096 Sep  3 08:27 .
drwxr-xr-x 5 mac mac 4096 Sep  3 08:27 ..
drwxr-xr-x 6 mac mac 4096 Sep  3 08:27 .git
```

### 1.2 First git status

```text
git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

### 1.3 After the first commit

```text
git status
On branch main
nothing to commit, working tree clean
```

### 1.4 git log

```text
git log --oneline
484fbf1 Create lab README
```

### 1.5 git diff

```text
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

````text
git diff
diff --git a/README.md b/README.md
index 6561b71..3536ae6 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 # Lab 03: Git and GitHub
 
+This repository documents my practice with local Git, GitHub, branches, and pull requests.
+
 ## README Responses
 
 ### 1.1 After initialization
@@ -29,8 +31,19 @@ nothing added to commit but untracked files present (use "git add" to track)
 
 ### 1.3 After the first commit
 
+```text
+git status
+On branch main
+nothing to commit, working tree clean
+```
+
 ### 1.4 git log
 
+```text
+git log --oneline
+484fbf1 Create lab README
+```
+
 ### 1.5 git diff
 
 Paste the `git status` and `git diff` commands and their output.
````

How does this `git status` differ from the one in **1.2**?

Between those two status checks, I staged and committed README.md, so Git began tracking it in the repository’s history. After I changed it again, Git reported it as modified because the current file differed from the version in the last commit.

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init` — it made the .git folder so git can track the files
- `git status` — it tells you which files changed and if they’re staged yet
- `git add` — it stages the file so it’s ready to be committed
- `git commit` — it saves the staged changes as a permanent snapshot with a message
- `git log` — it shows the commit history with ids and messages
- `git diff` — it shows the actual lines that changed not just the file name

### 1.7 Repository link

https://github.com/dmckenzi-star/lab03-exercises

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?

The outer loop selects a value, and the inner loop compares it with each value after it in that same list. If two values at different positions are equal, the program has found a duplicate. If it checks every pair without finding a match, there are no duplicates.

- How does the set-based approach check for a duplicate?

The function uses `seen` to remember values it has already encountered. For each value in the list, it checks whether that value is in `seen` **before adding it**. If it is already there, the value appeared earlier, so it is a duplicate. Otherwise, the function adds it to `seen` and continues. Reaching the end without a match means there are no duplicates.

- What is the runtime and memory trade-off of each?

For a list of n values, this takes **O(n) time on average**, because it makes one pass and set operations take constant time on average, but it needs **O(n) extra memory** in the worst case to store values. Nested loops take **O(n²) time in the worst case** but only **O(1) extra memory**, so the set approach trades additional memory for faster duplicate detection.

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge
