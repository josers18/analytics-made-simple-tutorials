"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Jev and TypeSafe AI: The Fast Decision Layer for Software
Canonical Article: https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/
License: MIT

Description:
A calibrated, 110ms customer refund and ticket triage service using TypeSafe AI
and Jev (the first System One decision model). Replaces brittle regular expressions
and slow 2,500ms LLM prompt-and-parse pipelines with fast, deterministic machine-native logic.
"""

import os
from dataclasses import dataclass
from typing import Optional

# Mock interface for TypeSafe SDK primitives
@dataclass
class DecisionResult:
    choice: str
    confidence: float
    reasoning_code: str

class TypeSafeClient:
    """TypeSafe AI decision layer client."""
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("TYPESAFE_API_KEY", "mock_key")

    def decide(self, context: dict, question: str, choices: list[str]) -> DecisionResult:
        """Execute calibrated System One judgment."""
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
