# TypeSafe AI Tutorial 1: Fast Customer Triage Engine

> **Official Companion Guide for [Analytics Made Simple: Jev and TypeSafe AI](https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/)**
> Raw Script: [`01_customer_triage_engine.py`](./01_customer_triage_engine.py)

Learn how to build high-speed (110ms), calibrated decision layers for production applications using System One models like Jev.

---

## Architectural Comparison

```text
Traditional LLM Pipeline (System Two):
User Input -> Construct Prompt -> LLM Generation (2,500ms) -> Regex/JSON Parsing -> Brittle Code

TypeSafe AI Pipeline (System One):
User Input + State -> Jev Calibrated Evaluation (110ms) -> Typed Choice + Confidence -> Deterministic Code
```

---

## The Complete Python Script

Below is the complete script contained in [`01_customer_triage_engine.py`](./01_customer_triage_engine.py):

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Fast Customer Triage Engine with TypeSafe AI (System One Jev)
Canonical Article: https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/
License: MIT
"""

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class DecisionResult:
    choice: str
    confidence: float
    reasoning_code: str

class TypeSafeClient:
    """Minimal simulation client demonstrating System One decision primitives."""
    def decide(self, context: Dict[str, Any], question: str, choices: List[str]) -> DecisionResult:
        text = str(context.get("message", "")).lower()
        if "refund" in text or "money back" in text or "charged twice" in text:
            return DecisionResult("refund_request", 0.96, "DEC_FIN_REFUND")
        elif "password" in text or "login" in text or "locked out" in text:
            return DecisionResult("account_access", 0.94, "DEC_AUTH_RESET")
        elif "broken" in text or "bug" in text or "error" in text:
            return DecisionResult("technical_issue", 0.91, "DEC_TECH_BUG")
        return DecisionResult("general_inquiry", 0.72, "DEC_GEN_SUPPORT")

def triage_incoming_ticket(customer_id: int, message: str, customer_tier: str) -> dict:
    """Triage incoming tickets with calibrated confidence gating."""
    client = TypeSafeClient()
    
    context = {
        "customer_id": customer_id,
        "message": message,
        "tier": customer_tier
    }
    
    decision = client.decide(
        context=context,
        question="What is the primary customer intent?",
        choices=["refund_request", "account_access", "technical_issue", "general_inquiry"]
    )
    
    # Fast deterministic routing logic based on calibrated confidence
    action = "escalate_to_human"
    if decision.confidence >= 0.90:
        if decision.choice == "refund_request" and customer_tier == "Enterprise":
            action = "auto_approve_immediate_credit"
        elif decision.choice == "account_access":
            action = "send_magic_reset_link"
        else:
            action = "route_to_specialized_queue"
            
    return {
        "customer_id": customer_id,
        "detected_intent": decision.choice,
        "confidence": decision.confidence,
        "reasoning_code": decision.reasoning_code,
        "automated_action": action
    }

if __name__ == "__main__":
    test_cases = [
        (101, "I was charged twice for subscription renew on invoice #901!", "Enterprise"),
        (102, "I forgot my password and cannot sign in on my mobile app.", "Standard"),
        (103, "Where do I find your office location?", "Standard")
    ]
    
    print("=== TypeSafe AI System One Triage Execution ===")
    for cid, msg, tier in test_cases:
        res = triage_incoming_ticket(cid, msg, tier)
        print(f"\nCustomer {res['customer_id']} ({tier}): '{msg}'")
        print(f"  -> Intent: {res['detected_intent']} (Confidence: {res['confidence']:.2f})")
        print(f"  -> Action: {res['automated_action']}")
```

---

## Expected Execution Output

```text
=== TypeSafe AI System One Triage Execution ===

Customer 101 (Enterprise): 'I was charged twice for subscription renew on invoice #901!'
  -> Intent: refund_request (Confidence: 0.96)
  -> Action: auto_approve_immediate_credit

Customer 102 (Standard): 'I forgot my password and cannot sign in on my mobile app.'
  -> Intent: account_access (Confidence: 0.94)
  -> Action: send_magic_reset_link

Customer 103 (Standard): 'Where do I find your office location?'
  -> Intent: general_inquiry (Confidence: 0.72)
  -> Action: escalate_to_human
```

---

## How to Run

```bash
python3 typesafe-ai/01_customer_triage_engine.py
```

👉 Next: [Part 2: Risk Scoring & Routing Pipeline](./02_sentiment_and_routing_pipeline.md)
