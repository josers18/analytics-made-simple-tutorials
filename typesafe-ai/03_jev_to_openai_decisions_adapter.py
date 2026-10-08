"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Alternatives to TypeSafe's Jev: paid and free AI models that make decisions compared
https://analyticsmadesimple.com/tutorials/jev-alternatives-paid-open-source-decision-models/
License: MIT

Run:     python3 03_jev_to_openai_decisions_adapter.py   (no key, no network, no installs)

Writes one ticket question in the Jev request shape, then rewrites it for the
OpenAI Decisions API. The Jev shape also works for Cloudflare Clef, AWS Strands
Decider, Laya and OpenJev, which accept the same request.
"""

# One ticket, three questions, written the Jev way.
# The same request works for Jev, Cloudflare Clef, Strands Decider, Laya and OpenJev.
jev_request = {
    "state": "Checkout has failed for every customer for the last hour.",
    "questions": {
        "urgent": {"type": "noul", "instructions": "Is this request urgent?"},
        "team": {
            "type": "choice",
            "instructions": "Which team should handle it?",
            "criteria": {"billing": "Charges and refunds", "technical": "Bugs and outages"},
        },
        "severity": {
            "type": "score",
            "instructions": "How bad is the customer impact?",
            "criteria": ["No impact", "Minor", "Major", "Critical"],
        },
    },
}


def to_openai(req):
    """Rewrite a Jev-style request in the OpenAI Decisions API shape."""
    questions = []
    for name, q in req["questions"].items():
        if q["type"] == "noul":
            questions.append({"name": name, "type": "predicate",
                              "instructions": q["instructions"]})
        elif q["type"] == "choice":
            questions.append({"name": name, "type": "choice",
                              "instructions": q["instructions"],
                              "choices": [{"value": k, "description": v}
                                          for k, v in q["criteria"].items()]})
        elif q["type"] == "score":
            questions.append({"name": name, "type": "score",
                              "instructions": q["instructions"],
                              "levels": [{"label": level} for level in q["criteria"]]})
    return {"model": "gpt-6-luna", "input": req["state"], "questions": questions}


openai_request = to_openai(jev_request)
print("Jev-style question types:", [q["type"] for q in jev_request["questions"].values()])
print("OpenAI question types:  ", [q["type"] for q in openai_request["questions"]])
print("OpenAI severity levels: ", openai_request["questions"][2]["levels"])
