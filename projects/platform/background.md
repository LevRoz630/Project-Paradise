---
layout: page
title: Background
permalink: /projects/platform/background/
---

[← Back to Platform]({{ '/projects/platform/' | relative_url }})

---

## Problem Statement

Student trading societies can't reliably use existing engines because high turnover, mixed skill levels, and laptop-based workflows make data handling, reproducibility, and standardized evaluation too hard to maintain.

Existing tools run strategies but assume students will build the missing infrastructure: versioned datasets, run provenance, comparable evaluation rules, and publish-ready reporting. Societies end up with one-off, non-reproducible backtests.

### The Gap

We need a **student-first platform layer** that standardizes:

| Component | Description |
|-----------|-------------|
| Curated Datasets | Validated historical data with versioning |
| Run Registry | Code/config/data provenance tracking |
| Evaluation Harness | Consistent metrics and assumptions |
| Reporting | Automatic publish-ready reports |
| Safe Deployment | Paper-first paths for broker connections |

---

## Existing Solutions

Most existing solutions are **engines** (they run strategies) or **commercial platforms** (they bundle data + infra but impose ecosystem constraints). Our project is a **student-first platform layer** that standardizes the workflow around an engine.

### LEAN (QuantConnect)

Open-source algorithmic trading engine for research, backtesting, and live trading.

| Strengths | Friction Points |
|-----------|-----------------|
| Full lifecycle: research → backtest → live | Ecosystem lock-in to QuantConnect |
| CLI support for local + cloud | Self-managed data + infra required locally |
| Ready-to-use datasets (commercial) | No standardized student workflow |

### NautilusTrader

Event-driven trading engine emphasizing research ↔ live parity.

| Strengths | Friction Points |
|-----------|-----------------|
| Clean architecture with standardized APIs | Engine-first, no student workflow layer |
| Exchange integrations (Binance) | Students must manage own data |
| Live trading parity | No reproducibility tracking |

---

## Our Approach

Build a lightweight platform layer on top of forked vectorbt that handles the student-specific needs: dataset versioning, run provenance, standardized evaluation, and publish-ready reporting.

See the [Development Outline]({{ '/projects/platform/outline/' | relative_url }}) for technical details.
