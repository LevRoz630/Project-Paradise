# Solutions on the market

Most existing solutions are **engines** (they run strategies) or **commercial platforms** (they bundle data + infra but impose ecosystem constraints). Our project is a **student-first platform layer** that standardizes the workflow around an engine: dataset handling, reproducibility, competition/evaluation, reporting, and safety defaults.

### 1) LEAN (QuantConnect)

> **TLDR**: LEAN is a strong engine; the missing layer for student clubs is a standardized, reproducible “course/competition workflow” on top of it.
> 

**What it is:** an open-source algorithmic trading engine designed for **research, backtesting, and live trading**, with integrations to data providers and brokerages; runs on **Windows/macOS/Linux** and supports **Python and C#**. 

**What it’s strong at:**

- Mature, full lifecycle engine: research → backtest → live
- A packaged CLI exists to run locally and/or sync with the cloud
- Broad ecosystem: QuantConnect also offers ready-to-use datasets and cloud infra (commercial)

**Where student societies hit friction (even though it’s powerful):**

- **Ecosystem orientation:** Many of the “batteries included” benefits (datasets marketplace, managed infra, cloud execution) are centered around QuantConnect’s environment. Running fully locally is possible but requires students to manage data + infra themselves (which becomes the real work).
- **Operational overhead for rotating cohorts:** Local use is feasible via CLI, but societies still need a consistent install/process across Windows machines, standardized datasets, and shared evaluation rules, none of which are enforced by the engine itself.

### 2) NautilusTrader

> **TLDR:** NautilusTrader is a stronger engine, however student societies need the reproducibility + standardization + sharing layer above the engine.
> 

**What it is:** an event-driven trading engine emphasizing **research ↔ live parity** and a normalized system API for integrations. 

**What it’s strong at:**

- Clean architecture for live trading nodes (data + execution clients + standardized APIs)
- Real exchange integrations exist (example: Binance integration supports both market data ingest and execution for spot and futures, with a structured set of adapter components).

**Where student societies hit friction:**

- **Engine-first, BYO workflow:** Nautilus provides the runtime and adapter patterns, but it does not provide a “student workflow” layer: dataset registry, run registry, standardized evaluation for competitions, and one-command reproducible reporting. Those are left to the user to build.
- **Data management is still your burden:** Even with great adapters, students must still source, clean, version, and standardize datasets to ensure comparability, especially if results are produced on personal laptops (which is typical in societies).
- **Reproducibility is not enforced:** Nautilus focuses on execution correctness, but it doesn’t automatically guarantee “every run has code+config+data identifiers logged and shareable” (what you need for publishing/competitions).

###