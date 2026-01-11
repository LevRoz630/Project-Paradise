---
layout: page
title: HKU x Avenir - Overview
---


[← Write-Ups]({{ '/competitions/write-ups/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }}) | [Team 2 Execution]({{ '/competitions/write-ups/hku/hku-ex-2/' | relative_url }})

---

## Round 1: Prediction

### Dataset

| Field | Value |
|-------|-------|
| Time Range | 2021-01-01 to 2024-12-31 |
| Source | Binance futures (OHLCV, non-anonymized) |
| Coins | 355 cryptocurrencies |
| Format | Parquet files |

### Objective

Predict 24-hour ahead returns at 15-minute intervals for all cryptocurrencies.

**Evaluation:** Weighted Spearman rank correlation (focus on extreme returns)

---

## Round 2: Live Trading

### Setup

| Field | Value |
|-------|-------|
| Teams | Top 15-30 advanced |
| Capital | $10,000 USD per team |
| Positions | Long/short real-time execution |

### Ranking Formula

| Component | Weight |
|-----------|--------|
| Sharpe Ratio | 40% |
| Return | 30% |
| Drawdown | 30% |

Lower score = better. Bonus: 20% of profits if max drawdown ≤ 15%

### Software Required

Lark, Yushu, QuantBase, GitLab, CrowdStrike

**Challenges:** Complex installation, 2FA slowed development, USB issues, watermarks on screen, no Linux support (used VM)
