---
layout: page
title: ML Research
permalink: /competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/mlresearch0-1-0/
---


[← Ideas]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## SmartXGB Performance Analysis

Evaluated model performance for 1h, 3h, 6h, 12h, 24h return targets with 6-fold CV.

| Spearman Mean | Spearman Std | Sign Accuracy Range |
|---------------|--------------|---------------------|
| 0.016 | 0.019 | 0.499 - 0.508 |
| 0.005 | 0.009 | 0.499 - 0.508 |
| 0.011 | 0.010 | 0.499 - 0.508 |
| 0.005 | 0.009 | 0.499 - 0.508 |
| 0.005 | 0.009 | 0.499 - 0.508 |

---

## Decision

Given:
- Poor results across all horizons
- Lack of clear research directions
- Complexity of well-performing models (from research papers)

**Decision:** Abandon ML path, focus on simpler, more interpretable and stable prediction techniques.
