---
layout: page
title: Infrastructure
---


## Concept

1. Features selected on 30-70% of data
2. Initial model selected from array on 30-70%
3. Grid Search with CV on 70-100%

General strategy: Independent selection of features and models with data overlaps. Models compared on same data for fair comparison. Best model selected from ~15 architectures and grid searched. Baseline approach due to data/time scarcity.

---

## backtester.py

[Workflow]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/infrastructure/workflow/' | relative_url }})

**Allows comparison of:**
- Sets of features
- Models

**Across:**
- Number of coins
- Data size

**Validation:** 5-fold CV returning Spearman value and optional p-value per symbol. Spearman calculated as decaying average over 96 periods (24 hours of 15min intervals). Decay accounts for noise likelihood over time.

---

## fsa_feature_importance.py

[Workflow]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/infrastructure/workflow/' | relative_url }})

Boruta method too complex with high computational demand. FSA chosen for different architecture not requiring iteration over N shadow features with repetitive RF fit.

---

## feature_test.py (Legacy)

**Feature Selection Method:**
- Feature importance
- Permutations

**Implementation:**
- Input feature functions to backtester
- Process selected coins through features
- Validate features for 96-step prediction

**Validation:**
- Rolling window-based permutation tests (MI changes)
- Returns proportion of permuted samples where MI > baseline as p-value
- Jaccard Stability
