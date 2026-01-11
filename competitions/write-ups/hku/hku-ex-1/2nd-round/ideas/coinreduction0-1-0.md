---
layout: page
title: Coin Reduction
---


[← Ideas]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Problem

SmartXGB predictions were insufficiently reliable for determining which coins to reduce.

---

## Solution

Adopted statistical filtering based on data quality and market conditions:

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| Training rows | ≥20,000 | Limited data undermines statistical validity |
| Trading volume | ≥70th percentile | Avoid illiquid markets |

---

## Risk Consideration

Low-volume environments combined with tight operational constraints (e.g., 9,000 stop-loss) increase the likelihood of illiquid conditions where positions become difficult to exit.
