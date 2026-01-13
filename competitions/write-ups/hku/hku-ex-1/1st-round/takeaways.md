---
layout: page
title: Takeaways
permalink: /competitions/write-ups/hku/hku-ex-1/1st-round/takeaways/
---


[← Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Infrastructure

| Improvement | Description |
|-------------|-------------|
| S3 Bucket | Cache CUDA Docker image for quick builds |
| GPU Optimization | Learn to optimize code for GPU on VMs |
| Scripts Directory | Create reusable utility scripts (feature selection, etc.) |
| Multiprocessing | Always multiprocess feature selection |
| Persistent Server | Digital Ocean ($4/month) for always-on access |

## Process

| Learning | Description |
|----------|-------------|
| Time Investment | Take more time for competitions - lack of time impacts performance AND enjoyment |
| Research vs Implementation | Balance meaningful research and hypothesis testing vs just implementing |
| Background Jobs | Use `nohup` for long-running calculations |

## Background Job Command

```bash
nohup python script.py > output.log 2>&1 &
```

| Flag | Purpose |
|------|---------|
| `nohup` | Ignore hangup signal |
| `> output.log` | Redirect stdout to log file |
| `2>&1` | Redirect stderr to stdout |
| `&` | Run in background |
