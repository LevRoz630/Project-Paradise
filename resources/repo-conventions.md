---
layout: page
title: Repo Conventions
permalink: /resources/repo-conventions/
---

[← Resources]({{ '/resources/' | relative_url }})

---

## Repository Structure

Every project follows a three-part structure:

| Component | Description |
|-----------|-------------|
| Code Repository | GitHub repo following conventions below |
| Data Storage | Git LFS for large files, or S3 bucket |
| Docker Environment | Containerized dev environment with all dependencies |

**Example:** [docker-hku ↗](https://github.com/LevRoz630/docker-hku){:target="_blank"}

---

## Why This Setup?

| Benefit | Description |
|---------|-------------|
| No System Bugs | Same dev environment eliminates "works on my machine" issues |
| Cloud Ready | Easy deployment to GPU servers like [vast.ai ↗](https://vast.ai/){:target="_blank"} |
| Industry Standard | Production-like environment gives you an edge in job applications |

---

## Git Workflow

### Branches

| Branch | Purpose |
|--------|---------|
| `main` | Protected, production-ready code |
| `develop` | Optional integration branch |
| `feature/*` | New features (e.g., `feature/signal-ema-tuning`) |
| `bugfix/*` | Bug fixes |
| `hotfix/*` | Urgent production fixes |
| `exp/*` | Experiments |

### Rules

| Rule | Description |
|------|-------------|
| Protected Branches | No direct pushes to `main` or `develop` |
| Pull Requests | All changes require PR with at least one reviewer |
| Commit Messages | Descriptive messages explaining what changed and why |
| Rebasing | Rebase on latest parent branch before PR to keep history linear |

---

## Package Management

**Preferred:** uv

**Alternatives:** poetry, venv

Every project must have a lock file that anyone can install to resolve dependencies consistently.

---

## Folder Structure

```
project-root/
├── README.md           # How to run/reproduce
├── pyproject.toml      # Dependencies + tooling
├── src/                # Clean, reusable code
├── tests/              # Test coverage (use pytest-cov)
├── examples/           # Usage examples and demos
```
