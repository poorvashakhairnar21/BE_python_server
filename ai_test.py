import os
from groq import Groq
from help import AI_PROMOT
from dotenv import load_dotenv
import json

load_dotenv()
AI_API_KEY = os.getenv("AI_API_KEY")

client_global = Groq(api_key=AI_API_KEY)

def get_reply(massage,client):
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

test_massage = test_cases = [
    # Exact command cases
    {"input": "code for reverse string", "output": ""}
]

with open("ai_responses.txt", "w") as file:
    for massage in test_massage:
        reply = get_reply("REAL MASSAGE:"+massage["input"],client_global)
        file.write(f"Input: {massage['input']}\nOutput: {reply}\n\n")
        reply_dict = json.loads(reply)
        print(dict(reply_dict))

# {"command": "set alarm", "parameters": {"time": "10:00"}}
# {"tends_task": "True", "comfirmation_massage": "Do you want to set the alarm for 07:00?", "command": "", "parameters": {}}
# {"tends_task": "False", "reply": "I'm good, how can I assist you?"}