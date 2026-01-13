---
layout: page
title: Moments Separation Implementation
permalink: /competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/momentsseparation/implementationmomentsseparation/
---


[← Moments Separation]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/momentsseparation/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Method

GMM on 6 months of data for 50 coins using:
- Rolling std
- Volatility ratio (std/mean)

GMM provides regime labels → validate with silhouette score → extract logic via tree classifier.

---

## Data Split

| Period | Usage |
|--------|-------|
| 2024-01 → 2024-06 | Training |
| 2024-06 → 2024-11 | Testing |

Sparse coins (e.g., TAOUSDT from 2024-03) use available data. Minimum: 7000 rows for train period.

---

## Experiment Results

### Run 1: Multiple Features

```python
feature_cols = ['returns_std_5', 'returns_std_60', 'volume_std_60',
               'returns_std_15', 'returns_std_30', 'volume_std_5',
               'volume_std_15', 'volume_std_30']
```

| Metric | 2 Clusters | 3 Clusters |
|--------|------------|------------|
| Mean Silhouette | 0.479 | 0.275 |
| Best Silhouette | 0.582 | 0.424 |
| Worst Silhouette | 0.383 | 0.148 |

### Run 2: Single Feature

```python
feature_cols = ['volume_std_30']
```

| Metric | Value |
|--------|-------|
| Mean Silhouette | 0.731 |
| Best Silhouette | 0.804 |
| Worst Silhouette | 0.642 |

**Strong separation achieved with single feature.**

---

## Validation

Tree classifier extracts boundaries. For coins without enough training data, use fallback rule:

```
mean(hist_std) + 0.5 * std  →  ~75% accuracy
```

---

## Feature Testing (H1)

| Model | Spearman Mean | Spearman Std |
|-------|---------------|--------------|
| LGBM_Basic | 0.0435 | 0.0171 |
| LGBM_Basic_Regimes | 0.0412 | 0.0194 |

**Next:** Separate data by regime in feature selector, run on same coins, compare selected features.
