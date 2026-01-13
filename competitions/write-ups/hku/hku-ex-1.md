---
layout: page
title: HKU Team 1 - Execution
---


[← Overview]({{ '/competitions/write-ups/hku/hku-ov/' | relative_url }}) | [Team 2 →]({{ '/competitions/write-ups/hku/hku-ex-2/' | relative_url }}) | [Code ↗](https://github.com/LevRoz630/docker-hku-avenir){:target="_blank"}

---

## Round 1

### Infrastructure

**Concept:** Independent feature and model selection with data overlaps

| Step | Data Range | Purpose |
|------|------------|---------|
| 1 | 30-70% | Feature selection |
| 2 | 30-70% | Initial model selection |
| 3 | 70-100% | Grid search with CV |

**Scripts:**

| File | Purpose | Details |
|------|---------|---------|
| `backtester.py` | Compare features/models | 5-fold CV, Spearman per symbol, decaying avg over 96 periods |
| `fsa_feature_importance.py` | Feature selection | FSA method (faster than Boruta) |

[Workflow Details]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/infrastructure/workflow/' | relative_url }})

---

### Research

| Topic | Link | Status |
|-------|------|--------|
| Preprocessing | [Notes]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/preprocessing/' | relative_url }}) | Z-score, Winsorization, Denoising explored |
| Model Selection | [Notes]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/model-selection/' | relative_url }}) | TimeGPT, LSTM, RF, custom models |
| Coins Grouping | [Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/coinsgroupinghypothesis0-1-0/' | relative_url }}) · [Findings]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/coinsgroupinghypothesis0-1-0/findings/' | relative_url }}) | Clustering by behavior |
| Exogenous Variables | [Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/exogenousvariables0-1-0/' | relative_url }}) | On-chain data, funding rates |
| Regimes | [Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/' | relative_url }}) · [Moments]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/regimeshypothesis0-1-0/momentsseparation/' | relative_url }}) | Market regime identification |
| Data Processing | [Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/dataprocessinghypothesis0-1-0/' | relative_url }}) · [NA Strategy]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/dataprocessinghypothesis0-1-0/na-missing/' | relative_url }}) | Missing data handling |

---

### Takeaways

[Full Takeaways]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/takeaways/' | relative_url }})

**Infrastructure:**
- S3 bucket for CUDA Docker caching
- GPU optimization
- Reusable scripts directory
- Multiprocess feature selection
- Digital Ocean persistent server ($4/month)

**Process:**
- More time for meaningful research
- Use `nohup python script.py > output.log 2>&1 &` for background calculations

---

## Round 2

### Infrastructure

[Details]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/infrastructure/' | relative_url }}) | [Changes from R1]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/infrastructure/infrachanges/' | relative_url }})

### Strategy Ideas

[All Ideas]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/' | relative_url }})

| Idea | Link | Result |
|------|------|--------|
| ML Research | [Notes]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/mlresearch0-1-0/' | relative_url }}) | Poor results, abandoned |
| Coin Reduction | [Notes]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/coinreduction0-1-0/' | relative_url }}) | Volume-based filtering |
| Cointegration | [Notes]({{ '/competitions/write-ups/hku/hku-ex-1/2nd-round/ideas/end-of-the-world/cointegration/' | relative_url }}) | Regime-based ECM approach |
