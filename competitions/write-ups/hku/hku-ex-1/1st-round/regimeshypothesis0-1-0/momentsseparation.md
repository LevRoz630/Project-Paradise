---
layout: page
title: Moments Separation
---


[← Regimes Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/' | relative_url }}) | **[Implementation]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/momentsseparation/implementationmomentsseparation/' | relative_url }})**

---

## Theory / Hypothesis

We suppose that coin statistical distributions (e.g. std and mean) change on average when a certain boundary is crossed.

**Example:** If for a period of time the coin's std is 2-3x greater than historical mean, we are in a regime where mean and std would be different.

**Hypothesis:** The correlation to features and types of features change - which could be checked by silhouette score.

---

## Process

1. Sample 50 coins
2. Find a discriminator for which statistical properties alter
3. Test on other part of data to check they alter sufficiently there as well
4. Measure if it's a good generalization

After features are received:
1. Use the measure to separate data into regimes on sample of coins and data
2. Run silhouette to verify separation by the change of correlation to the features
