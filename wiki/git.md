# GIT

## What is it?
Git is a distributed version control system. It allows us to keep track of our project recording every change made to our files over time, who made it, and why, creating a full, navigable history of the entire codebase. Every developer has a complete copy of the repository on their own machine, including the full history. This means you can work offline, commit changes locally, and only sync with others when you're ready.

## Why does it exist?
Before Git, teams working on the same codebase faced serious problems: overwriting each other's work, losing changes, having no way to go back to a previous version, or needing a central server just to do anything. Git was created in 2005 by Linus Torvalds (the creator of Linux) to solve exactly these problems for large-scale, distributed software development.

## Main concepts
-Repository (repo): the project folder that Git is tracking, containing all files and their complete history.
-Commit: a permanent snapshot of your changes at a given point in time, identified by a unique hash. The building block of Git history.
-Branch: an independent line of development. You can create branches to work on features or fixes in isolation, then merge them back when ready.
-Staging area: a middle layer between your working files and a commit. You explicitly choose what goes into each commit by staging changes first.
-Remote: a copy of the repository hosted on a server (like GitHub or GitLab) that the team uses to share and sync their work.
-Merge: the act of integrating the history of one branch into another, combining the work done in both.
-HEAD: a pointer that tells Git which commit or branch you're currently working on.

## Commands 
### git status
It allows us to know the current state of our working repository. Which branch are we on, which files have been modified (unready to commit),
which files are ready to commit (staging area), which files are untracked, if our branch is up to date ...
git status never modifies your repository. It is a read-only command and therefore completely safe to run at any time.

### git add
Moves changes from your working directory to the staging area, preparing them for the next commit.
git add does not create a commit. It only tells Git which changes should be included in the next commit.

### git commit 
Saves a permanent snapshot of everything in the staging area into your local repository's history.
A good commit should represent one logical unit of work a bug fix, a new feature, a refactor with a clear message explaining why the change was made, not just what changed.
A commit is a snapshot, not a backup.
#### Conventional Commits (git commit -m "Modification(spacework affected): message)
feat - Add a new functionality
fix - Fixing errors
perf - Performance improvements
refactor - Refactoring names
docs - Updates in any documentation
test - When adding unit tests

### git push
Uploads your local commits to a remote repository, making your work visible and shareable with others. Until you push, all your commits exist only on your machine. Under the hood, Git compares your local branch with the remote branch and sends only the difference the commits the remote doesn't have yet making it efficient even on large projects.

### git fetch
Downloads changes from a remote repository into your local machine, but it does not merge or apply them to your working directory. My current branch and files remain completely untouched. Think of it as "go check what's new on the remote and bring it locally, but don't touch my work yet."
This makes it the safest way to stay up to date, you can inspect what changed before deciding what to do with it.

### git checkout
Is one of Git's most versatile commands; it can switch branches, create new ones, or restore individual files to a previous state. In modern Git (2.23+) some of its responsibilities were split into git switch and git restore for clarity, but git checkout still works for all of them.

### git pull
Downloads changes from the remote and immediately integrates them into your current branch in a single step. It is essentially a shortcut for running git fetch followed by git merge (or git rebase, depending on the config).
It's the most common way to keep your local branch up to date with what your teammates have been pushing.
Because it changes your working tree, git pull may produce merge conflicts.

### git merge
Takes the history of one branch and integrates it into another. Unlike rebase, it preserves the full history of both branches by creating a new "merge commit" that ties them together.
It's the standard way to bring a finished feature branch back into main (or any other target branch).

## Common mistakes
### 403 Forbidden

**Cause**

Git Credential Manager is using credentials from another GitHub account.

**Solution**

1. Open Windows Credential Manager.
2. Remove the stored GitHub credential.
3. Run `git push` again.
4. Sign in with the correct GitHub account.

## Interview questions

## Personal notes