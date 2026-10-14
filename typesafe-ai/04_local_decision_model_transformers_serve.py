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
