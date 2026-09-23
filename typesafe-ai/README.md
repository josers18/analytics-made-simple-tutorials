# TypeSafe AI & System One Models

Code examples and decision engine architectures for [Jev and TypeSafe AI: The Fast Decision Layer for Software](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/).

---

## What is a System One Model?

While conversational chat models (System Two) generate human-like prose token-by-token over seconds, **System One models (like Jev)** output typed probabilistic decisions in **70 to 200 milliseconds** at a fraction of the cost ($0.042 per million input tokens).

### Key Decision Primitives:
1. **Choice:** Selects one option from a structured dictionary of criteria with normalized probabilities.
2. **Score:** Places inputs on a continuous spectrum between milestones.
3. **Noul:** Answers yes/no statements with calibrated, trustworthy probabilities (0.0 to 1.0).

---

## Example: Customer Triage & Automated Refund Service

[`customer_triage_engine.py`](./customer_triage_engine.py) demonstrates an automated customer support triage service. In under 50 lines of Python, it concurrently evaluates:
* **Intent:** Refund request vs cancellation vs technical support.
* **Agitation:** Frustration score along a continuous scale.
* **Policy Compliance:** Calibrated probability that the ledger shows a duplicate charge.

Execution time: **~112 milliseconds**.

```bash
pip install typesafe-sdk
python customer_triage_engine.py
```
