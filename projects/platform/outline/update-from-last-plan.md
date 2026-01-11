---
layout: page
title: Update from last plan
permalink: /projects/platform/outline/update-from-last-plan/
---

| Change | Description |
|--------|-------------|
| **Vectorbt Fork** | Fork vectorbt v1 and use its execution/trading logic as-is. Standardize assumptions: signals computed on bar close are **shifted +1** and executed at **next bar open**. Record all `from_signals` parameters, dataset hash, and dependency versions. |
| **Data Layer** | Data layer lives inside the vectorbt fork. Add missing sources (ccxt first) in `vectorbt.data`, all returning canonical OHLCV format. Toolkit repo stays thin. |
| **bttool Package** | Minimal orchestration: CLI (`bt run`, `bt list/show/diff`), deterministic resampling, artifact export + validation, versioned run store + registry, offline reports (HTML/PDF), and permutation testing. |
| **Scope Changes** | Regime detection removed from v1. ydata-synthetic simulation deferred to v2 (same data/artifact contracts maintained). |