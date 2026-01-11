---
layout: page
title: Exogenous Variables
---


[← Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Hypothesis

Dataset: 355 cryptocurrency pairs from Binance futures (CEX). DEX trades often indicate CEX market movements.

## Data Sources Explored

### On-Chain Data (Uniswap V2)

| Endpoint | Purpose |
|----------|---------|
| `liquiditypools` | Pool address mapping (tokens in wrapped state: WBTC, WETH) |
| `swaps/evm` | Historical swaps for pool address at timestamp |

API: TheGraph (supports Uniswap V2 since 2020, V3 since 2021)

### Binance Futures Data

| Variable | Description |
|----------|-------------|
| Funding Rate | Periodic payments between long/short |
| Open Interest | Total outstanding contracts |
| Long/Short Ratio | Market positioning |
| Buy/Sell Volume | Order flow |

### Sentiment Analysis

Potential for memecoins (pump and dump). Query social media (X, TruthSocial) → VADER NLP sentiment scoring.

**Practical concerns:** API costs, compute complexity.

---

## Result

**No exogenous data was used** due to lack of time for full validation of statistical significance and implementation stability.

Significant lagged correlation was found in futures data testing, but live implementation speed and value were not validated.
