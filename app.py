from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Get API Key from Environment Variable (More Secure)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ensure API key exists
if not GEMINI_API_KEY:
    raise ValueError("❌ Error: GEMINI_API_KEY is not set. Please set it before running the app.")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Check if API Key is set
    if not GEMINI_API_KEY:
        return jsonify({"reply": "Error: Gemini API key is missing."}), 500

    # Correct JSON format for Gemini API
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{
                "text": user_message
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 200
        }
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json=data)

    # Handle API response
    if response.status_code == 200:
        response_json = response.json()
        try:
            # Extract the bot's reply from the response
            bot_reply = response_json["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            bot_reply = "I'm sorry, I didn't understand."
    else:
        # Handle API errors
        bot_reply = f"Error: {response.json().get('error', {}).get('message', 'API request failed')}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
