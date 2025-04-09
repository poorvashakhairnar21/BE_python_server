import socket
from flask import Flask, request, jsonify
from flask_cors import CORS
from backend_request import get_ai_response
import json
from assitant_client.commands import COMMANDS

app = Flask(__name__)
CORS(app)  # Allow frontend requests (from React)

BACKEND_API_URL = "http://localhost:3001"

global pending_task
pending_task = {}

def do_client_task(analysis):
    command = analysis['command']
    parameters = analysis['parameters']
    command_execute, _ = COMMANDS.get(command, "")
    
    if command_execute:
        return jsonify({"reply": command_execute(**parameters)})
    else:
        return jsonify({"reply": "Command not found for task " + command})

@app.route("/chat", methods=["POST"])
def chat():
    global pending_task
    data = request.json
    user_message = data.get("message", "").strip().lower()
    user_previousChat = data.get("previousChat", "")
    user_isFirstMassage = str(data.get("isFirstMassage", False))
    
    try:
        analysis = json.loads(get_ai_response(user_message, user_previousChat, user_isFirstMassage, BACKEND_API_URL))
        title = analysis["title"]
    except (json.JSONDecodeError, TypeError) as e:
        return jsonify({"reply": "Sorry, I couldn't understand ,the response from AI.", "title": "none"})

    if 'tends_task' in analysis:
        if analysis['tends_task'] == 'True':
            pending_task = analysis
            return jsonify({"reply": analysis['comfirmation_message'], "title": title})
        else:
            temp_res = analysis['reply']
            if temp_res == "yes" and pending_task:
                response = do_client_task(pending_task)
                response_json = response.get_json()
                response_json["title"] = title
                pending_task = {}
                return jsonify(response_json)
            else:
                pending_task = {}
                return jsonify({"reply": temp_res, "title": title})
    else:
        pending_task = {}
        response = do_client_task(analysis=analysis)
        response_json = response.get_json()
        response_json["title"] = title
        return jsonify(response_json)

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))  # Bind to an available port
        return s.getsockname()[1]

if __name__ == "__main__":
    port = find_available_port()
    port = 3002
    print(f"Server starting on port {port}")
    app.run(debug=True, host="127.0.0.1", port=port)

 # {"command": "set alarm", "parameters": {"time": "10:00"}}
    # {"tends_task": "True", "comfirmation_massage": "Do you want to set the alarm for 07:00?", "command": "", "parameters": {}}
    # {"tends_task": "False", "reply": "I'm good, how can I assist you?"}

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=3002)