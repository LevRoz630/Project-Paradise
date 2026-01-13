---
layout: page
title: HKU Team 2 - Execution
permalink: /competitions/write-ups/hku/hku-ex-2/
---


[← Overview]({{ '/competitions/write-ups/hku/hku-ov/' | relative_url }}) | [Team 1]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Round 1: Model Development

### Approach

**Model:** XGBoost for non-linear relation capture while maintaining efficiency

| Parameter | Value |
|-----------|-------|
| Tree Construction | Histogram-based (faster, scalable) |
| Boosting Rounds | 300 |
| Max Depth | 6 |
| Learning Rate | 0.05 |

### Features (14 total)

| Category | Features |
|----------|----------|
| Momentum | RSI, 7d Momentum |
| Moving Average | MACD, EMA |
| Volatility | Bollinger Bands, Volatility (1d, 7d) |
| Volume | Average 7d Volume |
| Lagged Returns | 1hr, 4hr, 1d, 7d |

### Results

| Metric | Value |
|--------|-------|
| In-sample Weighted Spearman | 0.3113 |
| Out-of-sample Weighted Spearman | 0.1225 |

Gap suggests overfitting, but out-of-sample score remained strong given model simplicity.

---

## Round 2: Trading Strategy

### Design

**Threshold-Based Approach:**
- Trade only predicted returns > 2% magnitude
- 15-minute data (consistent with Round 1)
- Leverage model's accuracy on extreme predictions

**Position Sizing:**
- Weighted by prediction magnitude (not evenly distributed)
- Example: +5% predicted BTC return → larger BTC allocation

### Evolution

| Phase | Issue | Solution |
|-------|-------|----------|
| Initial | Underperformance after ~1 month | Insufficient diversification |
| Fix | Expanded trading list | Include maximum perpetuals |
| Oct 10 Crash | No extreme event handling | Added stop-loss: -2% long, +2% short |

### Future Improvements

- Replace fixed 2% threshold with volatility-based thresholds (Bollinger Bands)
- Implement ML-based stop-loss mechanisms
- Automate strategy parameters using indicators
