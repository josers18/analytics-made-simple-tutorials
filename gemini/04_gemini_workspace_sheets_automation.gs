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
