from flask import Flask, request, jsonify
from flask_cors import CORS
from backend_request import get_ai_response
import os
import json

app = Flask(__name__)
CORS(app)  # Allow frontend requests (from React)

BACKEND_API_URL = "http://localhost:3001"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip().lower()
    
    analysis = json.loads(get_ai_response(user_message,BACKEND_API_URL))
    # return jsonify({"reply": "testing"})
    
    if 'tends_task' in analysis:
        if analysis['tends_task'] == 'True':
            return jsonify({"reply": analysis['comfirmation_massage']})
        else:
            return jsonify({"reply": analysis['reply']})
    else:
        return jsonify({"reply": analysis})
    
    # {"command": "set alarm", "parameters": {"time": "10:00"}}
    # {"tends_task": "True", "comfirmation_massage": "Do you want to set the alarm for 07:00?", "command": "", "parameters": {}}
    # {"tends_task": "False", "reply": "I'm good, how can I assist you?"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3002)
