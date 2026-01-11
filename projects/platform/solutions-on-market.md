---
layout: page
title: Solutions on the market
permalink: /projects/platform/solutions-on-market/
---

Most existing solutions are **engines** (they run strategies) or **commercial platforms** (they bundle data + infra but impose ecosystem constraints). Our project is a **student-first platform layer** that standardizes the workflow around an engine: dataset handling, reproducibility, competition/evaluation, reporting, and safety defaults.

### 1) LEAN (QuantConnect)

> **TLDR**: LEAN is a strong engine; the missing layer for student clubs is a standardized, reproducible “course/competition workflow” on top of it.
> 

**What it is:** an open-source algorithmic trading engine designed for **research, backtesting, and live trading**, with integrations to data providers and brokerages; runs on **Windows/macOS/Linux** and supports **Python and C#**. 

**Strengths:**

| Feature | Description |
|---------|-------------|
| Full Lifecycle | Mature engine: research → backtest → live |
| CLI Support | Run locally and/or sync with cloud |
| Ecosystem | Ready-to-use datasets and cloud infra (commercial) |

**Friction Points:**

| Issue | Description |
|-------|-------------|
| Ecosystem Lock-in | Benefits centered around QuantConnect environment; local use requires self-managed data + infra |
| Operational Overhead | Societies need consistent install/process, standardized datasets, shared evaluation rules |

### 2) NautilusTrader

> **TLDR:** NautilusTrader is a stronger engine, however student societies need the reproducibility + standardization + sharing layer above the engine.
> 

**What it is:** an event-driven trading engine emphasizing **research ↔ live parity** and a normalized system API for integrations. 

**Strengths:**

| Feature | Description |
|---------|-------------|
| Clean Architecture | Live trading nodes with data + execution clients + standardized APIs |
| Exchange Integrations | Binance support for market data and execution (spot and futures) |

**Friction Points:**

| Issue | Description |
|-------|-------------|
| Engine-first | No student workflow layer: dataset registry, run registry, evaluation, reporting |
| Data Management | Students must source, clean, version, standardize datasets themselves |
| Reproducibility | Execution-focused; no automatic code+config+data provenance tracking |