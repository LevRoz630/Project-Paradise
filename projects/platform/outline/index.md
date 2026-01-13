---
layout: page
title: Outline
permalink: /projects/platform/outline/
---

### What this is

A student-first backtesting tool that handles reproducibility, standardized evaluation, and publish-ready reporting so teams can focus on research.

See [changes from last plan]({{ '/projects/platform/outline/update-from-last-plan/' | relative_url }}).

---

### For Students

| Benefit | Description |
|---------|-------------|
| Easy Setup | Works on any laptop, no complex infrastructure |
| Data Access | Built-in sources (ccxt, Yahoo Finance, CSV) |
| Reproducibility | Every run is versioned and traceable |
| Reports | Auto-generated HTML/PDF for sharing |
| Validation | Permutation testing to check significance |

---

### Core Components

| Component | Description |
|-----------|-------------|
| Backend | Forked vectorbt v1 for execution |
| Data Layer | Extended sources inside vectorbt |
| CLI Tool | `bt run`, `bt list`, `bt diff` commands |
| Artifacts | Standardized parquet/csv/json outputs |
| Reports | Offline HTML + PDF generation |

---

### Execution Model

| Rule | Description |
|------|-------------|
| Trading Logic | vectorbt as-is, no modifications |
| Bar Model | No intrabar dynamics or partial fills |
| Signal Timing | Computed on close, shifted +1, executed at next open |
| Versioning | Pin all dependencies, record data hash per run |

---

### Deliverables

| Deliverable | Description |
|-------------|-------------|
| Data Sources | CCXT integration inside vectorbt fork |
| Backtest Runner | Deterministic pipeline with signal alignment |
| Artifacts | `returns.parquet`, `equity.parquet`, `trades.csv`, `metrics.json` |
| Registry | Versioned run store with `run_id = sha256(config)` |
| Reports | HTML (Plotly) + PDF with equity, drawdown, distributions |
| Permutation Testing | Null distributions and p-values |

---

### Common Questions

| Question | Answer |
|----------|--------|
| Writing our own backend? | No, using vectorbt's tested execution |
| Why not use advanced platforms? | We prioritize interpretability and ease of contribution |
| Why not L2/L3 data? | Hard to access for students; OHLCV is sufficient for learning |
