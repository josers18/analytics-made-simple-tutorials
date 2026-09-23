# TypeSafe AI Tutorial 1: Fast Customer Triage Engine

> **Official Companion Guide for [Analytics Made Simple: Jev and TypeSafe AI](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/)**

Learn how to build high-speed (110ms), calibrated decision layers for production applications using System One models.

## Architectural Comparison

```text
Traditional LLM Pipeline (System Two):
User Input -> Construct Prompt -> LLM Generation (2,500ms) -> Regex/JSON Parsing -> Brittle Code

TypeSafe AI Pipeline (System One):
User Input + State -> Jev Calibrated Evaluation (110ms) -> Typed Choice + Confidence -> Deterministic Code
```

👉 Run script: `python3 typesafe-ai/01_customer_triage_engine.py`
