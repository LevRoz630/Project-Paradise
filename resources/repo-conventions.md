---
layout: page
title: Repo Conventions
permalink: /resources/repo-conventions/
---

# Repo Conventions

## General Structure

1. **Code GitHub Repository** made with conventions written below
2. **Git LFS (Large File Storage) if large swash of data is required** in a sister repository (migration to S3 for cost reasons to be tested)
3. **Docker File if required** that when built clones code and data repositories and sets up the development environment with all required packages and environmental variables, use fine-grained token to protect the development and share it individually with other members. See 
    
    https://github.com/LevRoz630/docker-hku#
    

### Why all of this?

1. Less debugging of system bugs (I can’t install it, I can’t launch it) due to same development environment
2. Ability to easily launch the code and use the processing power of the servers on services such as [https://vast.ai/](https://vast.ai/) in their Docker Instances 
3. Closer to industry standard production environment getting used to which would put you ahead of other applicants

## Git Conventions

- **Branches**: `main` protected; optional `develop`; short-lived `feature/*`, `bugfix/*`, `hotfix/*`, `exp/*` (e.g., `feature/signal-ema-tuning`)
- **Rules:** In any repository rules should be set to prohibit pushes to `main` and `develop` (if exists) without a PR with at least one reviewer
- **Commit style**: Descriptive, what has been to changed to allow quick reviews and easy-to-find history
- **Package Managing:** Preferably **uv** but any other alternative (e.g. poetry or venv works). Any project needs to have a lock file that can be installed by anybody in their virtual environment to resolve the packages (now it works on everyone’s machines).
- **Sync rules**: rebase on latest `main` or other parent branch before PR; keep history linear, e.g. if we branches are worked on and feature/one is merged into develop please first merge rebase develop into feature/one after which if feature/two needs to be merged, also rebase it off develop after merge of feature/one.
- **Folder Structure:** Will generally depend on the project and what needs to be done. Standard would be the following:
    
    project-root/
    ├─ [README.md](http://readme.md/)                # how to run/reproduce; leaderboard links
    ├─ pyproject.toml          # deps + tooling
    ├─ src/                        # key folder with clean code that is used in other parts of the application
    ├─ tests/             # tests the folder structure, for good development use covr to check test                                         coverage    
    ├─ examples/    # clear examples of what code does and why