---
layout: page
title: Coins Grouping Hypothesis v0.1.0
---


[← 1st Round]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/' | relative_url }}) | **[Findings]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/coinsgroupinghypothesis0-1-0/findings/' | relative_url }})**

---

## Hypothesis

Coins are **assumed** to have different relevant features.

We use hierarchical clustering on concurrent log returns to find similarities and groups which would be **assumed** to share the same dynamics.

---

## Outcome Paths

**If groups not found:**
- Look for another way to cluster (e.g. GMM that clusters based on distributions)
- Brute force groups through features selection per coin and group by that instead of indirect measures like return correlation
- OR use generalized features proven beyond reasonable doubt to represent the dataset

**If groups found:**
- Examine the feature groupings and sanity check them
- Run a feature brute force to detect the most significant relations
- See if the types of features and the correlation changes across groups

---

## Result

Not enough time to sort coins into proper groups - that would require training multiple models on different groups which would need to be tested and documented with each model taking more time to optimize.

While a good idea that would make sense to pursue to improve performance, we didn't have enough time for implementation. Other higher priority workflows took precedence.
