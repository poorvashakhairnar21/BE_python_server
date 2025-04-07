import requests

def get_ai_response(message: str, previousChat: list, API_URL:str) -> str:
    try:
        response = requests.post(f"{API_URL}/get-ai-reply", json={"message": message,"previousChat":previousChat})
        print(previousChat)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("reply", "No reply received")
    except requests.exceptions.RequestException as e:
        print("Error fetching AI response:", e)
        raise RuntimeError("Failed to fetch AI response") 