---
layout: page
title: Infrastructure Changes
permalink: /competitions/write-ups/hku/hku-ex-1/2nd-round/infrastructure/infrachanges/
---


[← Infrastructure]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/infrastructure/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Goal

Test model predictions using metrics **beyond weighted Spearman** before live trading.

| Question | Purpose |
|----------|---------|
| Which coins predict best? | Guide bet selection |
| How does horizon affect prediction? | 6h/12h/24h comparison |

Shorter horizons may capture more opportunities; longer horizons test robustness.

---

## Constraints

**No high-frequency trading** due to:
- Lack of order book data
- Unknown execution latency (instance → server → Binance)
