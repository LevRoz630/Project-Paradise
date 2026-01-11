---
layout: project
title: Outline
permalink: /projects/platform/outline/
---

# Outline

When confused see **Common Questions** section at the bottom of the page

Update

[Update from last plan](/projects/platform/outline/update-from-last-plan/)

## Scope (v1)

### Goal

Teaching-focused OHLCV backtesting + reporting tool that:

- uses **forked vectorbt v1** as the execution + data backend,
- adds missing **data sources inside vectorbt** (e.g., ccxt),
- runs on any resampled interval from a base dataset,
- exports standardized artifacts + schema validation,
- generates offline `report.html` + `report.pdf`,
- includes permutation testing,
- stores versioned runs via a registry.

### Key assumptions (vectorbt execution; must be documented + pinned)

- vectorbt trading logic is used as-is.
- bar-based model; no intrabar dynamics/partial fills.
- signals computed on close, **shifted +1**, executed at **next open** (open price series).
- vectorbt conflict rules and cost model fixed; record all `from_signals` params.
- pin vectorbt + dependencies; record versions + data hash per run.

---

## Deliverables (v1)

### D1 — Vectorbt fork: data sources

- Add missing sources (ccxt first) inside `vectorbt.data`.
- Ensure all sources return canonical OHLCV (`Open, High, Low, Close, Volume` + datetime index).
- Tests for data integrity + timezone + gap handling.

### D2 — Backtest runner (bttool)

- `bt run ...` loads from vectorbt source, resamples deterministically, generates signals, shifts them, runs `Portfolio.from_signals`.
- No custom execution logic beyond signal alignment + parameter lock-in.
- Deterministic outputs.

### D3 — Artifacts + validation (unchanged)

- `returns.parquet`, `equity.parquet`, `trades.csv`, `metrics.json`, `config.json`
- plus `versions.txt`
- Schema validation + tests.

### D4 — Versioned run store + registry

- `run_id = sha256(canonical_config.json)`
- `runs/<run_id>/...`
- registry index with key metrics + paths
- CLI: list/show/diff

### D5 — Offline report (artifacts-only)

- `report.html` (Plotly, embedded)
- `report.pdf` (HTML→PDF)
- sections: summary, equity/drawdown, return dist, rolling vol, trades, costs, permutation results.

### D6 — Permutation testing

- shuffle procedure defined and logged
- N reruns, store distributions, p-values
- integrated into artifacts + report.

---

## Minimal repo structure

```
repo/
  vectorbt/# forked upstream
    vectorbt/
      data/# add ccxt + new sources here
    tests/
    pyproject.toml

  bttool/
    bttool/
      cli.py
      assumptions.md
      backtest.py
      artifacts.py
      registry.py
      metrics.py
      permutation.py
      report.py
template.html
    tests/
      test_no_leakage_shift.py
      test_golden_run.py
    pyproject.toml

  runs/# gitignored

```

---

## 4-week plan (v1)

### Week 1: assumptions + vectorbt fork data + runner skeleton

- Write `assumptions.md`, embed into `config.json` + report.
- Implement ccxt source inside vectorbt fork + basic tests.
- Implement bttool runner: source → resample → signals → shift → from_signals.
- Artifact writer + validator.
- Run_id hashing + folder layout.
- Add “fail if not shifted” unit test.

**Acceptance:** deterministic run produces artifacts and passes no-leakage guard.

### Week 2: reporting + registry

- metrics module + `metrics.json`
- report.html from artifacts only
- registry index + `bt list/show/diff`
- report.pdf pipeline (Playwright/Chromium)

**Acceptance:** offline html/pdf and registry working.

### Week 3: permutations

- permutation executor (parallelizable)
- store distributions + p-values
- add report section

**Acceptance:** reproducible null distributions and significance reporting.

### Week 4: hardening

- golden dataset fixture + golden metrics hash
- CI + dependency pinning
- docs: adding a new vectorbt data source + strategy template

**Acceptance:** CI enforces determinism, schema, and no leakage.

### **Common Questions**

1. Are we writing the backend on our own?
    - No, we are using existing optimized and tested backend.
2. Why don’t you just use advanced platforms that already have reporting and all necessary tools included?
    - We are aiming for interpretability to create easy-to-learn toolkit rather than one-fits-all solution that would take tens of hours to learn and even more to be able to meaningfully contribute to
3. Why don’t you aim/adopt to use TOB (top of the book) or L2/L3 data?
    - That data is hard to access and usually requires perpetual hoarding (WebSockets) or sits behind paywalls, making it hard to get for an average student society unless they are serious about it at which point they might as well use more advanced tools.