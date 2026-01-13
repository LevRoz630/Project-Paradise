---
layout: page
title: Regimes Hypothesis v0.1.0
permalink: /competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/
---


[← 1st Round]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/' | relative_url }})

---

**[Hypothesis Implementation]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/hypothesisimplementation/' | relative_url }})** | **[Moments Separation]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/momentsseparation/' | relative_url }})**

---

## Process

Writing this while the feature selection across all coins is running.

After we will be able to pick the features that have the biggest impact on the market. That could also allow us to create groups of coins separated by the features for model tuning.

After features are selected we can examine how their behaviour changes when we use different measures to detect regimes. We can measure the wellness of the separation by a silhouette score.

We need an easy measure of separation such as `stdev > mu(stdev.rolling(n))` or similar to be implementable in the execution script.

After some attempts no meaningful separation was found by statistical properties, hence we are to wait for features where we could make an experiment with a selection of features and coins to find a good discriminant of regimes.

---

## Result

Regimes were found and with the tree model the thresholds exported, with 0.8 accuracy of the determination of the regime found by a GMM. It will be introduced as a feature to the implementation where after giving the dictionary with the threshold values, the code will be able to determine the regime at each point.
