# TypeSafe AI & System One Decision Engines

[![Track](https://img.shields.io/badge/Track-System%20One%20AI-purple.svg?style=flat-square)](https://analyticsmadesimple.com/tutorials/)
[![Models](https://img.shields.io/badge/Models-Jev%20%7C%20TypeSafe%20AI-black.svg?style=flat-square)](https://typesafe.ai)
[![Interactive Notebook](https://img.shields.io/badge/Jupyter-Decision%20Layer-blue.svg?style=flat-square)](./typesafe_ai_decision_layer.ipynb)

Official code companion for the TypeSafe AI and System One decision engine tutorials on [Analytics Made Simple](https://analyticsmadesimple.com).

---

## What is a System One Model?

While System Two models (like GPT-4, Claude 3.5 Sonnet, and Grok) excel at exploratory research and multi-step reasoning, they take **2,000–5,000ms** to generate tokens and require fragile prompt-and-parse loops.

**System One models (like Jev)** represent the fast, non-autoregressive decision layer for modern software:
* **Sub-150ms Latency:** Native execution suitable for real-time web requests and microservices.
* **Calibrated Confidence:** Yields real probabilities rather than uncalibrated logit guesses.
* **Typed Primitives:** Returns code-native types (`Choice`, `Score`, `Noul`) that plug directly into conditional application logic.

---

## Index of Implementations

| Project | Description | Script | Walkthrough | Article |
|:---|:---|:---:|:---:|:---:|
| **Customer Triage Engine** | 110ms ticket classification and auto-approval service | [`01_customer_triage_engine.py`](./01_customer_triage_engine.py) | [01_customer_triage_engine.md](./01_customer_triage_engine.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/) |
| **Risk Routing Pipeline** | Two-axis confidence gating for financial risk | [`02_sentiment_and_routing_pipeline.py`](./02_sentiment_and_routing_pipeline.py) | [02_sentiment_and_routing_pipeline.md](./02_sentiment_and_routing_pipeline.md) | [Read on AMS ↗](https://analyticsmadesimple.com/tutorials/) |
