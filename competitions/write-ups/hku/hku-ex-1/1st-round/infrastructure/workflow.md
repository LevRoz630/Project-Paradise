---
layout: page
title: Workflow
---


[← Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }}) | [Infrastructure]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/infrastructure/' | relative_url }})

---

## Method Selection

**Primary:** Boruta ([reference ↗](https://www.jstatsoft.org/article/view/v036i11){:target="_blank"}) - effective in DRW, strong conceptual foundation

**Alternative:** FSA ([paper ↗](https://arxiv.org/abs/2303.02223){:target="_blank"})

---

## Implementation Process

| Step | Description |
|------|-------------|
| Input | Feature functions + selected coin names (default: all) |
| Validation | Test feature relevance for 96 steps (24h of 15m intervals) |

---

## Boruta Feature Selection

| Component | Description |
|-----------|-------------|
| Method | Random Forest compares real vs permuted "shadow" features |
| Output | Features: Confirmed / Tentative / Rejected |
| Data | 60% temporal subsets (multiple stability checks) |
| Minimum | ≥100 clean samples required |

---

## MI Permutation Tests

| Step | Description |
|------|-------------|
| Baseline | Compute MI between feature and target |
| Resampling | Block bootstrap with adaptive blocks (min 16 periods = 4h) |
| Selection | Keep features with p-value ≤ 0.05 |

---

## Jaccard Stability Analysis

| Step | Description |
|------|-------------|
| 1. Subsample | 10 different 60% temporal subsets |
| 2. Pipeline | Run Boruta → MI permutation per subset |
| 3. Metric | Jaccard similarity (intersection/union) across subsets |
| 4. Final | Retain features appearing in ≥50% of runs |
