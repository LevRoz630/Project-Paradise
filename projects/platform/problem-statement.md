---
layout: page
title: Problem Statement
permalink: /projects/platform/problem-statement/
---

### TLDR:

Student trading societies can’t reliably use existing engines because high turnover, mixed skill levels, and laptop-based workflows make data handling, reproducibility, and standardized evaluation too hard to maintain. Existing tools run strategies but assume students will build the missing infrastructure: versioned datasets, run provenance, comparable evaluation rules, and publish-ready reporting, so societies end up with one-off, non-reproducible backtests. We are building the student-first platform layer that standardizes this workflow (and optionally synthetic market simulations) so students can learn, compete, and publish results consistently.

### Full Version:

Student quantitative trading societies need a way to produce **reproducible, comparable, and publishable** research outcomes despite operating under constraints that professional trading teams do not face: **high member turnover**, **mixed skill levels**, **limited time**, and **decentralized compute on personal (often Windows) laptops**. In practice, these constraints make it difficult to maintain consistent infrastructure, data pipelines, and evaluation standards across cohorts, leading to repeated “reinvention” each term and results that are often **one-off, irreproducible, and not comparable,** they are frequently relying on ad-hoc scripts and inconsistent data sources (e.g., scraped/free APIs) that break reproducibility and undermine competition integrity.

Existing solutions such as LEAN (QuantConnect) and NautilusTrader provide powerful **backtesting and execution engines**, but they assume users can build and maintain the surrounding workflow: **clean, versioned datasets; standardized validation and cost assumptions; run provenance tracking; reporting.** They also presume a full access to quality low-level data which students can hardly get their hands on. Commercial platforms may reduce some friction through managed infrastructure, but they often constrain local-first workflows and introduce costs that are difficult to justify for student groups, while still offering limited support for strategy validation beyond headline PnL.

The unmet gap is **student-first platform layer** that standardizes the full workflow needed for learning, competitions, and publishable research. This platform should provide: (1) curated and validated historical datasets with versioning; (2) an automatic run registry capturing code/config/data provenance; (3) a standardized evaluation harness with consistent metrics and assumptions; (4) automatic publish-ready reports; and (5) safe, paper-first deployment paths if/when broker connections are used.

Additionally, integrating **synthetic limit-order-book market simulation** enables university-wide competitions under controlled and repeatable market scenarios (stress regimes, low-liquidity environments, volatility shocks), allowing fair evaluation and deeper learning beyond fitting to historical data.

**References:** LOB Market Simulation (discontinued, documentation TBA)