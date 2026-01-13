### Git Basics
___
##### Quick links

* [<span style="color: seagreen; font-weight: bold;">What is Git?</span>](#what-is-git)
* [<span style="color: seagreen; font-weight: bold;">How to check if git is installed or not?</span>](#how-to-check-if-git-is-installed-or-not)
* [<span style="color: seagreen; font-weight: bold;">How to configure `git` on your device?</span>](#how-to-configure-git-on-your-device)
* [<span style="color: seagreen; font-weight: bold;">How to check which git profile is configured on the device?</span>](#how-to-check-which-git-profile-is-configured-on-the-device)
* [ <span style="color: seagreen; font-weight: bold;">How to create a `git repository`?</span>](#how-to-create-a-git-repository)
* [ <span style="color: seagreen; font-weight: bold;">Three important concecpts</span>](#three-important-concecpts )
* [ <span style="color: seagreen; font-weight: bold;">What is the basic Git work flow?</span>](#what-is-the-basic-git-work-flow)
* [ <span style="color: seagreen; font-weight: bold;">How to check the git status of the project?</span>](#how-to-check-the-git-status-of-the-project)
* [<span style="color: seagreen; font-weight: bold;">How to add files/changes to Git?</span> ](#how-to-add-files/changes-to-git )
* [<span style="color: seagreen; font-weight: bold;">How to commit changes in Git?</span> ](#how-to-commit-changes-in-git )
* [<span style="color: seagreen; font-weight: bold;">How to view the commit history?</span> ](#how-to-view-the-commit-history)
* [<span style="color: seagreen; font-weight: bold;">What is a `.gitignore` file?</span> ](#what-is-a-.gitignore-file)
* [<span style="color: seagreen; font-weight: bold;">How to create a `.gitignore` file?</span> ](#how-to-create-a-.gitignore-file )
* [<span style="color: seagreen; font-weight: bold;">How to check what is the current branch?</span>](#how-to-check-what-is-the-current-branch )
* [<span style="color: seagreen; font-weight: bold;">How to create a new branch?</span>](#how-to-create-a-new-branch)
* [<span style="color: seagreen; font-weight: bold;">How to switch to another branch?</span> ](#how-to-switch-to-another-branch)
* [<span style="color: seagreen; font-weight: bold;">How to merge a branch?</span>](#how-to-merge-a-branch )
* [<span style="color: seagreen; font-weight: bold;">How to add a project to a repository?</span>](#how-to-add-a-project-to-a-repository )
* [<span style="color: seagreen; font-weight: bold;">How to check an existing remote repository?</span> ](#how-to-check-an-existing-remote-repository)
* [<span style="color: seagreen; font-weight: bold;">How to push files to git repository?</span>](#how-to-push-files-to-git-repository)
* [<span style="color: seagreen; font-weight: bold;">How to pull latest code from git?</span>](#how-to-pull-latest-code-from-git)
* [<span style="color: seagreen; font-weight: bold;">How to undo file edits (before stagging)?</span>](#how-to-undo-file-edits-before-stagging)
* [<span style="color: seagreen; font-weight: bold;">How to undo the last commit?</span>](#how-to-undo-the-last-commit)
* [<span style="color: seagreen; font-weight: bold;">What to do for adding project to GitHub repository for the first time?</span>](#what-to-do-for-adding-project-to-github-repository-for-the-first-time )
* [<span style="color: seagreen; font-weight: bold;">What to do for adding project to an existing GitHub repository for second time?</span>](#what-to-do-for-adding-project-to-an-existing-github-repository-for-second-time)
* [<span style="color: seagreen; font-weight: bold;">What to do for adding project to an existing GitHub repository from a new folder or new machine?</span>](#what-to-do-for-adding-project-to-an-existing-github-repository-from-a-new-folder-or-new-machine)
* [<span style="color: seagreen; font-weight: bold;">What's the recommended workflow with branches in git and GitHub?</span>](#whats-the-recommended-workflow-with-branches-in-git-and-github)


##### What is Git? [\*](#git-basics)
A version control system. Git and GitHub is not the same. `Git` is a tool on the computer, and `GitHub` is a tool for online hosting of Git repositories.

##### How to check if `git` is installed or not? [\*](#git-basics)
```bash
git --version
```

##### How to configure `git` on your device? [\*](#git-basics)
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

##### How to check which git profile is configured on the device? [\*](#git-basics)
```bash
git config --list
```

##### How to create a `git repository`? [\*](#git-basics)

Option A: Start `git` in an existing project:

```bash
cd my_project
git init

# Now this folder is a git repository
```

Option B: Clone from GitHub:

```bash
git clone https://github.com/username/repo-name.git
```

##### Three important concecpts

| Concecpt	| Meaning	|
|-----------|-----------|
| `Working Directory` | Your files |
| `Stagging Area` | Files ready to configure |
| `Repository` | Saved history |

##### What is the basic Git work flow? [\*](#git-basics)

`Edit/Change -> Add -> Commit -> Push`

##### How to check the git status of the project? [\*](#git-basics)
```bash
git status

# This tells:
#	Which files changed
#	Which are stagged
#	What Git expects next
```

##### How to add files/changes to Git? [\*](#git-basics)

```bash
git add file.txt 	# add file.txt
git add . 			# add all files
```

##### How to commit changes in Git? [\*](#git-basics)

```bash
git commit -m "comment to pass"
```

##### How to view the commit history? [\*](#git-basics)

```bash
git log
git log --oneline	# short version
```

##### What is a `.gitignore` file? [\*](#git-basics)

A `.gitignore` file is a plain text file in a Git repository that specifies which files and directories should be intentionally untracked and ignored by Git. It helps keep the repository clean and prevents the accidental inclusion of unnecessary, temporary, or sensitive files.

##### How to create a `.gitignore` file? [\*](#git-basics)

```bash 
touch .gitignore

# example .gitignore:
#	env/
#	node_modules/
#	__pycache__/
#	db.sqlite3
#	.env
```

##### How to check what is the current branch? [\*](#git-basics)

```bash
git branch
```

##### How to create a new branch? [\*](#git-basics)

```bash
git branch branch_name
```

##### How to switch to another branch? [\*](#git-basics)

```bash
branch checkout another_branch

# or
branch checkout -b branch_name
# this will create+switch to a new branch
```

##### How to merge a branch? [\*](#git-basics)

```bash
# go to main branch
git checkout main

# merge 'feature-login' branch
git merge feature-login
```

##### How to add a project to a repository? [\*](#git-basics)

```bash
git remote add origin https://github.com/username/repo-name.git
```

##### How to check an existing remote repository? [\*](#git-basics)

```bash
git remote -v
```

##### How to push files to git repository? [\*](#git-basics)

```bash
git push -u origin main

# after first push
git push
```

##### How to pull latest code from git? [\*](#git-basics)

```bash
git pull
# always pull before starting work
```

##### How to undo file edits (before stagging)? [\*](#git-basics)

```bash
# undo mistakes before stagging
git checkout -- file.txt

# undo mistakes in the stagging area
git reset file.txt
```

##### How to undo the last commit? [\*](#git-basics)

```bash
# keep the changes
git reset --soft HEAD~1

# delete the changes
git reset --hard HEAD~1

# Be careful with 'hard'!
```

##### What to do for adding project to GitHub repository for the first time? [\*](#git-basics)

```bash
# go to your project folder
cd my_project

# initialise git
git init

# create `.gitignore` - very important
touch .gitignore

# check status
git status

# stage files
git add .	# or specific file

# first commit
git commit -m "Initial commit"

# Create repository on GitHub

# Connect local repo to GitHub
git remote add origin https://github.com/username/repo-name.git

# verify
git remote -v

# push to GitHub
git branch -M main
git push -u origin main
```

##### What to do for adding project to an existing GitHub repository for second time? [\*](#git-basics)

```bash
# pull latest changes first
git pull

# work on your files

# check changes
git status

# stage changes
git add . 	# or specific file

# commit changes
git commit -m "Add dashboard UI for managers"

# push
git push -u origin main
# or, `git push` for later use
```

##### What to do for adding project to an existing GitHub repository from a new folder or new machine? [\*](#git-basics)

```bash
# clone the project first
git clone https://github.com/username/repo.git
cd repo

# then, pull
git pull

# the rest is as recommended earlier
```

##### What's the recommended workflow with branches in git and GitHub? [\*](#git-basics)

```bash
# create feature branch
git checkout -b feature-dashboard

# edit → commit → push
git add .
git commit -m "Create dashboard layout"
git push -u origin feature-dashboard

# then, on GitHub repository, open Pull Request, and merge with 'main' branch
git checkout main
git merge feature-dashboard

# this would be an IMPRESSIVE way of work
```
