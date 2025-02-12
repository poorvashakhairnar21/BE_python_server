from flask import Flask, request, jsonify
from flask_cors import CORS
# from assitant_client.commands import COMMANDS
import os
from groq import Groq
from dotenv import load_dotenv
from help import AI_PROMOT
import json

load_dotenv()
AI_API_KEY = os.getenv("AI_API_KEY")
client_global = Groq(api_key=AI_API_KEY)

def get_ai_analysis(massage,client):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": AI_PROMOT+" "+massage,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

app = Flask(__name__)
CORS(app)  # Allow frontend requests (from React)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip().lower()
    
    analysis = json.loads(get_ai_analysis('REAL MASSAGE: '+user_message,client_global))
    # return jsonify(analysis)
    
    if 'tends_task' in analysis:
        if analysis['tends_task'] == 'True':
            return jsonify({"reply": analysis['comfirmation_massage']})
        else:
            return jsonify({"reply": analysis['reply']})
    else:
        return jsonify({"reply": "Asking to do task."})
    
    # {"command": "set alarm", "parameters": {"time": "10:00"}}
    # {"tends_task": "True", "comfirmation_massage": "Do you want to set the alarm for 07:00?", "command": "", "parameters": {}}
    # {"tends_task": "False", "reply": "I'm good, how can I assist you?"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3002)
