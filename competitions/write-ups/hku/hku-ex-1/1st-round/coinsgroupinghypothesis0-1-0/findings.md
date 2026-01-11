---
layout: page
title: Coin Grouping Findings
---


[← Coins Grouping Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/coinsgroupinghypothesis0-1-0/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Hierarchical Clustering Results

Used hierarchical clustering on scaled returns, creating groups.

### 5 Clusters → 3 Clusters → 4 Clusters

Testing different cluster counts revealed **at least 2 distinct clusters**:
- Cluster 4: behavior similar to Cluster 3
- Cluster 2: totally different behavior

### Cluster Characteristics

| Cluster | Description |
|---------|-------------|
| 1 | Low to middle-low volume |
| 2 | Shitcoins + stablecoin (DFUSDT, DEXEUSDT, HIVEUSDT, PHAUSDT, UXLINKUSDT, USDCUSDT) |
| 4 | Solid coins with big volumes |

---

## Time-Based Correlation Analysis

Explored changes in correlation between coins - better measure of evolving relationships than overall correlation trend.

**Method:** Monthly correlation changes over 12 months

**Result:** Very similar behavior across clusters - may not be significant when derived this way.

### Cluster Statistics (Normalized)

| Cluster | Close Price Mean | Std | Volume Mean | Std |
|---------|------------------|-----|-------------|-----|
| 1 | -0.0 | 0.999 | -0.0 | 0.999 |
| 2 | -0.0 | 0.997 | 0.0 | 0.997 |
| 3 | -0.0 | 0.999 | 0.0 | 0.999 |
| 4 | 0.0 | 0.997 | -0.0 | 0.997 |

---

## Conclusion

Insufficient time to implement proper coin grouping. Would require training multiple models per group with individual optimization - deprioritized in favor of other workflows.
