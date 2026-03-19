---
layout: page
title: Durak Reinforcement Learning
permalink: /projects/durak-rl/
description: "Training RL agents via self-play to master the imperfect-information card game Durak using a C++ game engine and Python training pipeline."
---

[← Back to Projects]({{ '/projects/' | relative_url }})

<span class="badge">C++</span> <span class="badge">Python</span> <span class="badge">Reinforcement Learning</span>

---

## What We're Building

| | |
|---|---|
| **Type** | Learning project |
| **Focus** | Reinforcement learning and agentic modelling |
| **Final Product** | Playable game against trained RL agents |
| **Repo** | [durak-reinforcement-learning ↗](https://github.com){:target="_blank"} |

---

## Architecture

- **C++ Game Engine** — Durak rules, game state, legal actions, step function. Exposed to Python via pybind11.
- **Python Training** — PyTorch neural networks trained through self-play using the C++ engine for fast simulation.
- **Frontend** — UI to play against trained agents (TBD).

---

## Skills / Want to Learn

<span class="badge">Reinforcement Learning</span> <span class="badge">Self-Play</span> <span class="badge">C++</span> <span class="badge">pybind11</span> <span class="badge">PyTorch</span> <span class="badge">Game Theory</span> <span class="badge">Imperfect Information Games</span>
