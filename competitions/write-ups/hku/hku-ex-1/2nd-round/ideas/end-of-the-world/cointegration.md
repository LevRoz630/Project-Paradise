---
layout: page
title: Cointegration
permalink: /competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/end-of-the-world/cointegration/
---


[← Ideas]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Hypothesis

Check if coin relationships (beta) change depending on market regime. Current pairs may not be cointegrated in all regimes, but others might be.

---

## Regime Features (per symbol, stationary)

| Feature | Description |
|---------|-------------|
| `r_t` | 15m log-return |
| `\|r_t\|` | Absolute return |
| `vol_1d` | Rolling std over 1 day (96 bars) |
| `vol_1w` | Rolling std over 7 days |
| `z1d` | Rolling z-score over 1 day |

Normalize with StandardScaler per symbol; clip outliers.

---

## Labeling Process

| Step | Description |
|------|-------------|
| 1. Fit HMM | Per-symbol GaussianHMM on feature matrix |
| 2. Select states | n_states ∈ {2,3,4} by val loglik/BIC |
| 3. Predict | state_t for each timestamp |
| 4. Build labels | Wide format: `SYMBOL_hmm_state` columns |

---

## Cointegration Testing

Pass regime labels to `test_baskets_cointegration_parallel()`:
- Filter rows by basket states before Johansen test
- Policy: 'all' states or specific include_states
