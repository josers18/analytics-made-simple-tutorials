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
