---
layout: page
title: Model Selection
---


[← 1st Round]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/' | relative_url }})

---

## Foundational Models

Work comparatively well with lack of data, outperformed by DL (e.g. LSTM) otherwise.

- TimeGPT
- TCN
- 1-d CNNs

---

## Hybrid (LSTM + GRU)

Combines architectures for long/short term forecasting.

Reference: [Attention-Based Transformer + GRU Model for Predicting Cryptocurrency Prices](https://arxiv.org/abs/2504.17079){:target="_blank"}

---

## LSTM

Reference: [A Cryptocurrency Price Prediction Model using Deep Learning](https://www.researchgate.net/publication/371309639_A_Cryptocurrency_Price_Prediction_Model_using_Deep_Learning){:target="_blank"}

---

## Random Forest

Reference: [Integrated Framework for Cryptocurrency Price Forecasting](https://www.mdpi.com/2076-3417/15/4/1864){:target="_blank"}

---

## AR + L1 + L2 Regularization

Found going through papers on energy balancing market forecasting. The market data is highly complex and easy to overfit so could be good for our use case.

---

## Custom Anti-Overfit Model

Custom model written for DRW Crypto (performed best then). Caution: Competition was with CS data.
