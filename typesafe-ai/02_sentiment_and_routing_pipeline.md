# TypeSafe AI Tutorial 2: Risk Scoring & Routing Pipeline

> **Official Companion Guide for [Analytics Made Simple: System One Models](https://analyticsmadesimple.com/tutorials/)**
> Raw Script: [`02_sentiment_and_routing_pipeline.py`](./02_sentiment_and_routing_pipeline.py)

Explore two-axis confidence gating and deterministic branching for fraud and risk management.

---

## The Complete Python Script

Below is the complete script contained in [`02_sentiment_and_routing_pipeline.py`](./02_sentiment_and_routing_pipeline.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: System One Decision Layers for Routing
Canonical Article: https://analyticsmadesimple.com/tutorials/
License: MIT
"""

def evaluate_risk_and_route(transaction_id: str, amount: float, account_age_days: int) -> dict:
    """Evaluate financial transaction risk with two-axis confidence gating."""
    # Fast decision heuristic mapping System One model outputs
    is_high_amount = amount > 5000.0
    is_new_account = account_age_days < 14
    
    if is_high_amount and is_new_account:
        risk_score = 0.94
        decision = "flag_manual_review"
    elif is_high_amount:
        risk_score = 0.65
        decision = "require_2fa_step_up"
    else:
        risk_score = 0.08
        decision = "auto_approve"
        
    return {
        "transaction_id": transaction_id,
        "amount": amount,
        "account_age_days": account_age_days,
        "risk_confidence": risk_score,
        "routing_decision": decision
    }

if __name__ == "__main__":
    txs = [
        ("TX-801", 6200.00, 3),
        ("TX-802", 7500.00, 180),
        ("TX-803", 45.00, 450)
    ]
    for tid, amt, age in txs:
        print(evaluate_risk_and_route(tid, amt, age))
```

---

## Expected Output

```json
{'transaction_id': 'TX-801', 'amount': 6200.0, 'account_age_days': 3, 'risk_confidence': 0.94, 'routing_decision': 'flag_manual_review'}
{'transaction_id': 'TX-802', 'amount': 7500.0, 'account_age_days': 180, 'risk_confidence': 0.65, 'routing_decision': 'require_2fa_step_up'}
{'transaction_id': 'TX-803', 'amount': 45.0, 'account_age_days': 450, 'risk_confidence': 0.08, 'routing_decision': 'auto_approve'}
```

---

## How to Run

```bash
python3 typesafe-ai/02_sentiment_and_routing_pipeline.py
```

👉 Explore the interactive notebook: [typesafe_ai_decision_layer.ipynb](./typesafe_ai_decision_layer.ipynb)
