# ChatGPT Tutorial 4: Custom GPT Action OpenAPI Schema

> **Official Companion Guide for [Analytics Made Simple: Custom GPTs Tutorial](https://analyticsmadesimple.com/series/chatgpt/)**
> Raw Schema: [`04_custom_gpt_action_openapi_schema.json`](./04_custom_gpt_action_openapi_schema.json)

Custom GPTs become true enterprise agents when connected to live databases via OpenAPI 3.1 Actions.

---

## The Complete OpenAPI 3.1 Specification

Below is the production-ready Action schema contained in [`04_custom_gpt_action_openapi_schema.json`](./04_custom_gpt_action_openapi_schema.json):

```json
{
 "openapi": "3.1.0",
 "info": {
  "title": "Analytics Made Simple Data Warehouse API",
  "description": "Custom GPT Action schema for querying verified company metrics and order records.",
  "version": "1.0.0"
 },
 "servers": [
  {
   "url": "https://api.analyticsmadesimple.com/v1"
  }
 ],
 "paths": {
  "/metrics/summary": {
   "get": {
    "operationId": "getMetricsSummary",
    "summary": "Retrieve high-level business performance indicators",
    "parameters": [
     {
      "name": "period",
      "in": "query",
      "required": true,
      "schema": {
       "type": "string",
       "enum": [
        "current_quarter",
        "prior_quarter",
        "ytd"
       ]
      }
     }
    ],
    "responses": {
     "200": {
      "description": "Summary metrics payload",
      "content": {
       "application/json": {
        "schema": {
         "type": "object",
         "properties": {
          "revenue": {
           "type": "number"
          },
          "active_clients": {
           "type": "integer"
          },
          "order_volume": {
           "type": "integer"
          }
         }
        }
       }
      }
     }
    }
   }
  }
 }
}
```

---

## Instructions for Custom GPT Configuration

When setting up your GPT in the ChatGPT Builder (**Configure** tab):
1. **Name:** Weekly Analytics Officer
2. **Instructions:**
   ```text
   You are an analytical assistant answering leadership questions.
   Use the 'getMetricsSummary' action to retrieve verified numbers before answering revenue or client volume questions.
   If the API returns an error, report the error state rather than hallucinating plausible figures.
   ```
3. **Actions:** Click **Create new action**, then copy the JSON schema above into the **Schema** box.

👉 Explore the interactive notebook: [chatgpt_data_analysis_cookbook.ipynb](./chatgpt_data_analysis_cookbook.ipynb)
