# One request shape for Jev and its alternatives

> **Official companion for [Alternatives to TypeSafe's Jev: paid and free AI models that make decisions compared](https://analyticsmadesimple.com/tutorials/jev-alternatives-paid-open-source-decision-models/)**
> Raw script: [`03_jev_to_openai_decisions_adapter.py`](./03_jev_to_openai_decisions_adapter.py)

Jev, Cloudflare Clef, AWS Strands Decider, Laya and OpenJev all accept the same request: a `state` (the text to judge) and a `questions` map. The OpenAI Decisions API asks the same three kinds of question with different field names. This script writes one support-ticket request the Jev way and rewrites it for OpenAI, so the rest of your program never has to know which vendor answered.

It runs offline. There is no API key, no network call, and nothing to install.

## How the two shapes line up

| What it is | Jev, Clef, Strands, Laya, OpenJev | OpenAI Decisions API |
|---|---|---|
| Yes-or-no question | `noul` | `predicate` |
| List of options | `criteria` (name: description) | `choices` (`value`, `description`) |
| Ordered scale | `criteria` (list of levels) | `levels` (`label`, `description`) |
| The text to judge | `state` | `input` |
| Where questions go | `questions` (keyed by name) | `questions` (list, each with a `name`) |
| Address | `/v1/systemone` | `/v1/decisions` |

Field names come from the [TypeSafe models page](https://docs.typesafe.ai/models.md), the [Cloudflare Clef model page](https://developers.cloudflare.com/workers-ai/models/clef/) and the [OpenAI Decisions guide](https://developers.openai.com/api/docs/guides/decisions), checked October 8, 2026. The Decisions API was in public beta that day, so check the guide before you rely on these names.

## The script

```python
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
```

## What each part does

1. **`jev_request`** holds one ticket ("Checkout has failed for every customer for the last hour") and three questions: a yes-or-no (`noul`), a pick-one (`choice`) with two teams, and a rating (`score`) on a four-level scale. This exact dictionary is what you would send to Jev, Clef, Strands Decider, Laya or OpenJev.
2. **`to_openai`** walks the questions and renames the parts OpenAI spells differently. A `noul` becomes a `predicate`. A choice's `criteria` dictionary becomes a `choices` list of `value` and `description`. A score's list of levels becomes `levels`, one `label` each. The ticket text moves from `state` to `input`, and the model is set to `gpt-6-luna`, the only model the Decisions API accepts.
3. **The prints** show the question types before and after, and the rebuilt severity scale, so you can see the rewrite without sending anything.

Keep a function like `to_openai` in one place. Swapping vendors then means changing an address and a key, not every call site.

## Expected output

```text
Jev-style question types: ['noul', 'choice', 'score']
OpenAI question types:   ['predicate', 'choice', 'score']
OpenAI severity levels:  [{'label': 'No impact'}, {'label': 'Minor'}, {'label': 'Major'}, {'label': 'Critical'}]
```

## How to run

```bash
python3 03_jev_to_openai_decisions_adapter.py
```

Python 3.8 or newer. Standard library only.

To send the requests for real, post `jev_request` to your Jev, Clef or local server address, or `openai_request` to OpenAI's `/v1/decisions`, with that service's key. Images work on Clef and OpenAI only, and both want the image bytes inside the request, not a link.

## Next

- [Route a payment from a choice and a score](./02_sentiment_and_routing_pipeline.md), a live Jev call with the TypeSafe SDK.
- [Back to the TypeSafe and Jev module](./README.md)
