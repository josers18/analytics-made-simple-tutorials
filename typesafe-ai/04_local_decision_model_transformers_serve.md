# How to run your own decision model for free with Hugging Face transformers

> Companion code for the Analytics Made Simple guide: [How to run your own decision model for free with Hugging Face transformers](https://analyticsmadesimple.com/tutorials/run-your-own-decision-model-transformers-serve/)

> Raw Script: [`04_local_decision_model_transformers_serve.py`](./04_local_decision_model_transformers_serve.py)

`transformers serve` has a `/v1/systemone` endpoint that turns an open chat model into a decision model on your own computer. You send text, a question, and the answers you allow. It returns a probability for each answer without writing any text. This script uses it to route support tickets, and passes the unsure ones to a bigger model and then to a person.

As of October 14, 2026 the endpoint is only on the transformers `main` branch (merged October 12 in [PR 49322](https://github.com/huggingface/transformers/pull/49322)); the latest PyPI release, 5.19.0, does not have it yet.

## How it flows

```text
ticket ──> small model (Qwen2.5-1.5B) ── confidence >= 0.80 ──> team
                    │
                    └─ below 0.80 ──> big model (Qwen2.5-7B) ── >= 0.80 ──> team
                                              │
                                              └─ below 0.80 ──> person
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install torch "transformers[serving] @ git+https://github.com/huggingface/transformers.git"
transformers serve          # leave this running; it loads each model on first use
```

The small model is 2.9 GB on disk and the 7B model 14 GB. Both download automatically on first use.

## One question with curl

```bash
curl -s http://localhost:8000/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-1.5B-Instruct",
    "state": "I was charged twice for my October invoice.",
    "questions": {
      "team": {
        "type": "choice",
        "instructions": "Which team should handle this support ticket?",
        "criteria": {
          "billing": "Charges, refunds, invoices or payment methods",
          "technical": "Bugs, errors, outages or integration problems",
          "account": "Logins, passwords, users or plan changes"
        }
      }
    }
  }'
```

Output (probabilities rounded):

```json
{
  "model": "Qwen/Qwen2.5-1.5B-Instruct",
  "answers": {
    "team": {
      "type": "choice",
      "choice": "billing",
      "probabilities": {
        "billing": 0.999985,
        "technical": 1e-05,
        "account": 5e-06
      },
      "confidence": 0.999977
    }
  },
  "usage": {
    "input_tokens": 104,
    "output_tokens": 0
  }
}
```

## The script

```python
# Analytics Made Simple (analyticsmadesimple.com)
# Tutorial: How to run your own decision model for free with Hugging Face transformers (https://analyticsmadesimple.com/tutorials/run-your-own-decision-model-transformers-serve/)
# License: MIT
#
# Routes practice support tickets with a small local open model through `transformers serve`
# (POST /v1/systemone). Unsure answers go to a bigger local model, and if that is unsure
# too, to a person.
# Start the server first, in another terminal (it loads each model on first use):
#   transformers serve
import json
import sys
import urllib.error
import urllib.request

URL = "http://localhost:8000/v1/systemone"
SMALL = "Qwen/Qwen2.5-1.5B-Instruct"
BIG = "Qwen/Qwen2.5-7B-Instruct"  # set to None to skip the second model
BAR = 0.80  # below this confidence, pass the ticket on

TEAMS = {
    "billing": "Charges, refunds, invoices or payment methods",
    "technical": "Bugs, errors, outages or integration problems",
    "account": "Logins, passwords, users or plan changes",
    "other": "Anything that fits none of the teams above",
}

TICKETS = [
    "I was charged twice for my October invoice.",
    "Our integration has been failing for 3 days and we are losing sales!",
    "How do I add a new user to our team plan?",
    "The export button gives an error 500 every time.",
    "I forgot my password and the reset email never arrives.",
    "Can I get a refund for the seats we did not use?",
    "Your app is slow and my card was declined when I tried to upgrade.",
    "Do you have an office in Berlin?",
]


def decide(ticket, model):
    body = {
        "model": model,
        "state": ticket,
        "questions": {
            "team": {"type": "choice", "instructions": "Which team should handle this support ticket?", "criteria": TEAMS}
        },
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["answers"]


def main():
    try:
        urllib.request.urlopen("http://localhost:8000/health", timeout=5)
    except (urllib.error.URLError, OSError):
        print("No server at localhost:8000. Start it with: transformers serve")
        sys.exit(1)
    print(f"{'ticket':<52} {'team':<10} {'conf':>5}  route")
    for t in TICKETS:
        a = decide(t, SMALL)["team"]
        route = a["choice"]
        if a["confidence"] < BAR and BIG:
            b = decide(t, BIG)["team"]
            route = f"{b['choice']} (big model)" if b["confidence"] >= BAR else "person"
        elif a["confidence"] < BAR:
            route = "person"
        print(f"{t[:50]:<52} {a['choice']:<10} {a['confidence']:5.2f}  {route}")


if __name__ == "__main__":
    main()
```

### What each part does

| Part | What it does |
|---|---|
| `TEAMS` | The allowed answers and a one-line description of each. The `other` option matters: without it the small model put "Do you have an office in Berlin?" under technical. |
| `decide()` | Sends one ticket and one `choice` question to `/v1/systemone` with Python's built-in `urllib`, and returns the `answers` object. |
| `BAR` | The confidence below which a ticket is passed on. Pick it from your own labelled tickets, not from this example. |
| `SMALL` / `BIG` | The first model and the one that handles the unsure cases. Set `BIG = None` to send unsure tickets straight to a person. |
| `main()` | Checks the server is up (and stops with a message if not), then prints team, confidence and route for each ticket. |

## Output

Run on an Apple M5 Max Mac on October 14, 2026, with the server already running:

```text
ticket                                               team        conf  route
I was charged twice for my October invoice.          billing     1.00  billing
Our integration has been failing for 3 days and we   technical   1.00  technical
How do I add a new user to our team plan?            account     1.00  account
The export button gives an error 500 every time.     technical   1.00  technical
I forgot my password and the reset email never arr   account     1.00  account
Can I get a refund for the seats we did not use?     billing     0.90  billing
Your app is slow and my card was declined when I t   account     0.40  billing (big model)
Do you have an office in Berlin?                     other       0.91  other
```

With the server's default settings, the 1.5B model answered each ticket in about 0.03 seconds and the 7B model in about 5 seconds, which is why only the unsure ticket goes to the 7B model.

## How to run

```bash
python3 04_local_decision_model_transformers_serve.py
```

## Next

- [Test whether a cheaper AI decision model is good enough](https://analyticsmadesimple.com/tutorials/test-cheaper-ai-decision-model-decision-bench/): build the labelled test set that tells you where to put `BAR`.
