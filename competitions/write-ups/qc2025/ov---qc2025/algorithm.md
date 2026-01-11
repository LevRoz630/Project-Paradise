---
layout: page
title: QC2025 Basketball Algorithm
---


3 deadlines total - one for each game/evaluation round. Template provided with functions to be extended:

![Template functions](./image.png)

## Core Concept

Basketball-style trading simulation: Buy when market probability is "too low" (market underpredicts home team win), short when "too high" (market overpredicts). Key focus: accurately evaluating winning probability for any home vs away matchup.

**Data available:** Live game events containing event type (shot, rebound, null), score, time remaining

**Ideas considered:** Bayesian updating (market probability as prior), reinforcement learning, time-remaining probability adjustments

## Possession-Based Strategy

**Final approach:** Model the game using possessions

**Key elements:**
- Each possession: 4 outcomes [0, 1, 2, 3] points
- Team's average possession time and score → score per second
- Public basketball stats → weights for possession outcomes
- Individual player game-day performance → fitness adjustments (implemented but unused)

## Trading Mechanics

Contracts return 100 if home team wins:
- Buy at 50, home wins: +50 profit
- Buy at 50, home loses: -50 loss
- Short at 50, home wins: -50 loss
- Short at 50, home loses: +50 profit

---

## Key Functions

### kelly_fraction

Calculates capital share for trade execution:

```python
def _kelly_fraction(self, p: float, price: float, cap: float) -> float:
    if price <= 0 or price >= 100:
        return 0.0
    b_home = 100.0 / price - 1.0
    num_home = p * b_home - (1.0 - p)
    if num_home > 0 and b_home > 0:
        f = num_home / b_home
        return max(0.0, min(f, cap))
    price_away = 100.0 - price
    if price_away <= 0 or price_away >= 100:
        return 0.0
    b_away = 100.0 / price_away - 1.0
    num_away = (1.0 - p) * b_away - p
    if num_away <= 0 or b_away <= 0:
        return 0.0
    f_away = num_away / b_away
    return -max(0.0, min(f_away, cap))
```

### mc_winprob

Monte-Carlo rollouts estimating home-win probability. Simulates game continuations using team scoring baselines from recent possessions:

```python
def _mc_winprob(self, poss, now_time_seconds, player_stats, trials=500, baseline_frac=0.2):
    total_game_seconds = self._detect_total_game_seconds()
    if not poss:
        home_base = {"p_score": 0.35, "pi_pos": [0.06, 0.62, 0.32]}
        away_base = {"p_score": 0.35, "pi_pos": [0.06, 0.62, 0.32]}
    else:
        k = max(1, int(len(poss) * baseline_frac))
        recent = poss[-k:]
        home_base = self._fit_recent(recent, "home", frac=1.0)
        away_base = self._fit_recent(recent, "away", frac=1.0)
    # ... simulation logic ...
    return wins / trials
```

### suggest_trade

Trade decision based on game state, market price, and model probabilities:

```python
def _suggest_trade(self, poss, now_time_seconds, market_price):
    p_market = float(market_price) / 100.0
    n_poss = len(poss)
    # Weight market vs model (early game: trust market more)
    if n_poss < 3: w_market = 0.9
    elif n_poss < 6: w_market = 0.5
    else: w_market = 0.0

    p_model = self._mc_winprob(poss, now_time_seconds, self._player_stats)
    blended_p = (w_market * p_market) + ((1.0 - w_market) * p_model)
    f = self._kelly_fraction(blended_p, market_price, cap=self.max_fraction)
    stake = f * self.bankroll
    return {"fraction": f, "stake": stake}
```
