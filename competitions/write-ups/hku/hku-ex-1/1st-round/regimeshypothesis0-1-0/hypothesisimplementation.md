---
layout: page
title: Regimes Implementation
permalink: /competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/hypothesisimplementation/
---


[← Regimes Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Hypothesis

From [TwoSigma competition](https://medium.com/kaggle-blog/two-sigma-financial-modeling-code-competition-5th-place-winners-interview-team-best-fitting-279a493c76bd){:target="_blank"}: solution benefited from basing models and weightings on different market regimes (relying more on Ridge than tree in volatile periods).

**Application:** Detect where/in which regimes models perform best.

---

## Approach Options

| Option | Description |
|--------|-------------|
| Regimes vs Groupings | Compare significance of regimes vs crypto groupings |
| Regime Features | Use regime changes for feature detection |
| Weighted Spearman | Features predicting price spikes benefit competition score |

---

## Implementation Pipeline

```
Data → Coin Dummies → Train model(s) per version → Regime Dummies → Execute with weighted outputs
```

Possible to have regimes within large groups.

---

## Key Insight

May make sense to use regimes for feature detection: spot features that perform well across all regimes when samples might be dominated by some specific regime.
