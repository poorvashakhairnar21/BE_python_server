import requests

API_URL = "http://localhost:3002"

def get_ai_response(message: str) -> str:
    try:
        response = requests.post(f"{API_URL}/chat", json={"message": message})
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("reply", "No reply received")
    except requests.exceptions.RequestException as e:
        print("Error fetching AI response:", e)
        raise RuntimeError("Failed to fetch AI response") from e

massage = "play song"

print(get_ai_response(massage))