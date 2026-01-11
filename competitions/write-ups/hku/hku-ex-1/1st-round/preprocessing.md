---
layout: page
title: Preprocessing
---


[← Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Methods Evaluated

| Method | Assessment | Reference |
|--------|------------|-----------|
| Z-score | Uncertain effectiveness | [MDPI Paper ↗](https://www.mdpi.com/2076-3417/15/4/1864){:target="_blank"} |
| Change Point Detection (PELT) | Too complex | [ResearchGate ↗](https://www.researchgate.net/publication/371309639){:target="_blank"} |
| Winsorization | Needs experiment | Previous DRW experience |
| Denoising Autoencoder | Not implementable | [arXiv ↗](https://arxiv.org/pdf/2412.18202){:target="_blank"} |

## Result

Selected **Iterative Cross-Sectional Standard Scaler** to prevent data leak. Winsorization was too cumbersome to implement iteratively.
