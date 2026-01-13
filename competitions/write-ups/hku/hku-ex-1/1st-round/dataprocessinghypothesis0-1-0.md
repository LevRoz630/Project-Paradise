---
layout: page
title: Data Processing Hypothesis v0.1.0
permalink: /competitions/write-ups/hku/hku-ex-1/1st-round/dataprocessinghypothesis0-1-0/
---


[← 1st Round]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/' | relative_url }}) | **[NA Investigation]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/dataprocessinghypothesis0-1-0/na-missing/' | relative_url }})**

---

## Goal

Compare methods of handling outliers in the training data.

We probably won't be able to meaningfully predict extreme spikes regardless, so it makes sense to filter them in training data.

**Winsorization** - preferred method as tested in DRW comp where it significantly improved stability and predictive power of the model (even though result was measured with Spearman not weighted Spearman).

---

## Result

Iterative Cross-Sectional Standard Scaler (prevents data leak). Iterative Winsorization took too much time and was cumbersome to implement, hence was discarded.
