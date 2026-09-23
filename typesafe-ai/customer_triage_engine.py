#!/usr/bin/env python3
"""
Customer Triage & Automated Refund Service
Powered by Jev (TypeSafe AI System One Model)

Tutorial: https://analyticsmadesimple.com/tutorials/jev-typesafe-ai-system-one-model-rlcd-tutorial/
"""

import os
from typesafe_sdk import TypeSafeClient, Choice, Score, Noul

# 1. Assemble structured state payload
customer_state = {
    "ticket": {
        "id": "TICK-9042",
        "customer_tier": "enterprise_gold",
        "message": (
            "Your system charged our corporate card $499 twice for invoice INV-2024-09. "
            "We only authorized a single charge. Please reverse the duplicate payment immediately."
        )
    },
    "billing_ledger": {
        "invoice_id": "INV-2024-09",
        "authorized_amount": 499.00,
        "recorded_charges": [
            {"charge_id": "ch_101", "amount": 499.00, "status": "captured", "timestamp": "2026-09-20T14:10:02Z"},
            {"charge_id": "ch_102", "amount": 499.00, "status": "captured", "timestamp": "2026-09-20T14:10:05Z"}
        ]
    },
    "refund_policy": (
        "Duplicate charges occurring within a 60-second window for the same invoice "
        "are classified as processing errors and are eligible for instant automated reversal."
    )
}

# 2. Define parallel questions using typed primitives
triage_questions = {
    "primary_intent": Choice(
        instructions="What is the primary request in `ticket.message`?",
        criteria={
            "refund_request": "Customer explicitly demands return of funds or duplicate charge reversal",
            "subscription_cancellation": "Customer wants to terminate service or close account",
            "technical_support": "Customer reports software bugs, outage, or broken features",
            "general_inquiry": "Customer requests documentation, pricing details, or receipts"
        }
    ),
    "customer_frustration": Score(
        instructions="Score the level of customer agitation in `ticket.message`",
        criteria=[
            "Calm, neutral, and matter-of-fact",
            "Firm and concerned, but civil",
            "Severely agitated, threatening cancellation or legal action"
        ]
    ),
    "policy_eligible_refund": Noul(
        instructions=(
            "Does `billing_ledger.recorded_charges` demonstrate a duplicate charge "
            "eligible for immediate refund under `refund_policy`?"
        )
    )
}

def main():
    print("Sending evaluation request to Jev System One engine...")
    with TypeSafeClient() as client:
        response = client.system_one(
            state=customer_state,
            questions=triage_questions
        )

    intent = response.answers["primary_intent"]
    frustration = response.answers["customer_frustration"]
    refund_eligibility = response.answers["policy_eligible_refund"]

    print(f"\n[Decisions Returned in ~110ms]")
    print(f"Primary Intent: {intent.choice} (Confidence: {intent.confidence:.2f})")
    print(f"Frustration Score: {frustration.score:.2f} / 2.0 (Confidence: {frustration.confidence:.2f})")
    print(f"Policy Refund Probability: {refund_eligibility.noul:.2f}")

    # Deterministic software branching
    print("\n[Application Execution]")
    if intent.choice == "refund_request" and refund_eligibility.noul > 0.90:
        dup_charge = customer_state["billing_ledger"]["recorded_charges"][1]["charge_id"]
        print(f"SUCCESS: High-confidence duplicate charge verified (>90%). Triggering automated payment reversal for {dup_charge}...")
    elif frustration.score > 1.5:
        print("ESCALATION: Customer is severely agitated. Paging high-priority Tier-2 on-call...")
    else:
        print("ROUTING: Assigning ticket to standard customer billing queue.")

if __name__ == "__main__":
    main()
