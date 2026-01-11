---
layout: page
title: Data Source
permalink: /projects/platform/data-source/
---

[← Platform]({{ '/projects/platform/' | relative_url }}) | [Outline]({{ '/projects/platform/outline/' | relative_url }})

---

## Supported Data Sources

| Source | Type | Status |
|--------|------|--------|
| CCXT | Crypto exchanges | In development |
| Yahoo Finance | Equities, ETFs | Planned |
| Custom CSV | User data | Supported |

---

## Data Format

All sources return canonical OHLCV format:

| Column | Description |
|--------|-------------|
| Open | Opening price |
| High | Highest price |
| Low | Lowest price |
| Close | Closing price |
| Volume | Trading volume |

*Documentation in progress*