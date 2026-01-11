---
layout: page
title: NA / Missing Data
---


[← Data Processing Hypothesis]({{ '/competitions/write-ups/hku/hku-ex-1/1st-round/dataprocessinghypothesis0-1-0/' | relative_url }}) | [Team 1 Execution]({{ '/competitions/write-ups/hku/hku-ex-1/' | relative_url }})

---

## Empty Symbol Files

Recent coins with no data (models should not be restrictive with names):

DUSDT, SUSDT, ALCHUSDT, COOKIEUSDT, SOLVUSDT, PROMUSDT, BIOUSDT, AVAAIUSDT, SWARMSUSDT, PIPPINUSDT, ANIMEUSDT, SONICUSDT, ARCUSDT, GRIFFAINUSDT, TRUMPUSDT

---

## VWAP Missing Data

| Symbol | NaN % | Action |
|--------|-------|--------|
| TLMUSDT | 11.48% | Investigate |
| ICPUSDT | 8.17% | Investigate |
| CVCUSDT | 0.01% | ffill/fillna(0) |
| SCUSDT | 0.01% | ffill/fillna(0) |
| CTKUSDT | 0.007% | ffill/fillna(0) |
| RAYUSDT | 0.007% | ffill/fillna(0) |
| STRAXUSDT | 0.007% | ffill/fillna(0) |
| WAVESUSDT | 0.006% | ffill/fillna(0) |
| BLZUSDT | 0.006% | ffill/fillna(0) |
| LITUSDT | 0.005% | ffill/fillna(0) |

**TLMUSDT and ICPUSDT** need investigation due to high missing percentage. Rest can be handled with `ffill()` or `fillna(0)`.
