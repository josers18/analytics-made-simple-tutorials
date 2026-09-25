# Gemini Tutorial 4: Google Sheets & Workspace Automation

> **Official Companion Guide for [Analytics Made Simple: Gemini Workspace](https://analyticsmadesimple.com/series/gemini/)**
> Raw Script: [`04_gemini_workspace_sheets_automation.gs`](./04_gemini_workspace_sheets_automation.gs)

Bridge Google Sheets directly to Gemini with Google Apps Script, enabling `=GEMINI_CLASSIFY()` formulas across massive spreadsheets.

---

## The Complete Apps Script

Below is the JavaScript contained in [`04_gemini_workspace_sheets_automation.gs`](./04_gemini_workspace_sheets_automation.gs):

```javascript
/**
 * Analytics Made Simple (analyticsmadesimple.com)
 * Tutorial: Gemini for Google Sheets & Workspace Automation
 * Series: Gemini Workspace Tutorial
 * License: MIT
 */

/**
 * Custom Google Sheets Function to query Gemini models directly from cells.
 * Usage: =GEMINI_CLASSIFY("acme industrial corp", "Extract clean company name and strip legal suffixes")
 */
function GEMINI_CLASSIFY(inputText, promptInstruction) {
  if (!inputText) return "";
  
  var apiKey = PropertiesService.getScriptProperties().getProperty("GEMINI_API_KEY");
  if (!apiKey) {
    return "Error: Set GEMINI_API_KEY in File > Project properties";
  }
  
  var url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=" + apiKey;
  
  var payload = {
    "contents": [{
      "parts": [{
        "text": promptInstruction + "\nInput text: " + inputText
      }]
    }]
  };
  
  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload),
    "muteHttpExceptions": true
  };
  
  try {
    var response = UrlFetchApp.fetch(url, options);
    var json = JSON.parse(response.getContentText());
    if (json.candidates && json.candidates[0].content.parts) {
      return json.candidates[0].content.parts[0].text.trim();
    }
    return "Error: No candidate returned";
  } catch (e) {
    return "Error: " + e.toString();
  }
}
```

---

## Setup in Google Sheets

1. Open your Google Sheet.
2. Navigate to **Extensions** → **Apps Script**.
3. Paste the code above into `Code.gs`.
4. Go to **Project Settings** (gear icon) → **Script Properties** → Add `GEMINI_API_KEY` with your API key from Google AI Studio.
5. In any cell, run:
   ```text
   =GEMINI_CLASSIFY(A2, "Standardize into a clean company name")
   ```

👉 Explore the interactive notebook: [gemini_long_context_analytics.ipynb](./gemini_long_context_analytics.ipynb)
