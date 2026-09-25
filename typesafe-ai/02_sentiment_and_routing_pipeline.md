# Route a payment from a choice and a score

> **Official companion for [System One models](https://analyticsmadesimple.com/tutorials/system-one-models-fast-decision-layer-for-software/)**
> Raw script: [`02_sentiment_and_routing_pipeline.py`](./02_sentiment_and_routing_pipeline.py)

The model returns a route and a risk score. The `if` reads `response.choices['route']`. It does not decide the route by comparing the dollar amount itself.

## The script

```python
"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Route a payment with a System One choice and score
https://analyticsmadesimple.com/tutorials/system-one-models-fast-decision-layer-for-software/
License: MIT

Install: pip install typesafe-sdk
Run:     export TYPESAFE_API_KEY=... && python3 02_sentiment_and_routing_pipeline.py

Jev picks the route and the risk score. The if-statement only reads those fields.
The script stops when the key or the SDK is missing.
"""

import os
import sys


def main() -> None:
    if not os.environ.get("TYPESAFE_API_KEY"):
        sys.exit("Set TYPESAFE_API_KEY and run again.")
    try:
        from typesafe_sdk import Choice, Score, TypeSafeClient
    except ImportError:
        sys.exit("Install the SDK first: pip install typesafe-sdk")

    state = {
        "transaction_id": "TX-801",
        "amount": 6200.00,
        "account_age_days": 3,
        "note": "New account. Wire to a first-time beneficiary, requested by email at 02:14.",
    }
    questions = {
        "route": Choice(
            instructions="Where should this payment go, given `amount`, `account_age_days`, and `note`?",
            criteria={
                "auto_approve": "Small, ordinary payment on an established account",
                "step_up": "Large payment that still fits the account history",
                "manual_review": "New account, unusual hour, or a first-time beneficiary",
            },
        ),
        "risk": Score(
            instructions="How risky is this payment?",
            criteria=[
                "Ordinary spend on a known account",
                "Larger than usual, but the account history still fits",
                "New account or a first-time destination that a person should see",
            ],
        ),
    }
    with TypeSafeClient() as client:
        response = client.system_one(state=state, questions=questions)

    route = response.choices["route"]
    risk = response.scores["risk"]
    print(f"Route: {route.choice} (Confidence: {route.confidence:.2f})")
    print(f"Risk score: {risk.score:.2f} / 2.0 (Confidence: {risk.confidence:.2f})")
    if route.choice == "manual_review" and route.confidence >= 0.80:
        print("Action: queue_for_a_person")
    else:
        print(f"Action: {route.choice}")


if __name__ == "__main__":
    main()
```

## How to run

```bash
pip install typesafe-sdk
export TYPESAFE_API_KEY=your_key
python3 02_sentiment_and_routing_pipeline.py
```

If the key or the SDK is missing, the script stops. It does not print a made-up answer.



## Next

[Back to the folder](./README.md)
