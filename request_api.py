import requests

CLIENT_API_URL = "http://localhost:3002"

def get_client_response(message: str,API_URL:str) -> str:
    try:
        response = requests.post(f"{API_URL}/chat", json={"message": message})
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("reply", "No reply received")
    except requests.exceptions.RequestException as e:
        print("Error fetching AI response:", e)
        raise RuntimeError("Failed to fetch AI response") 

massage = "open notepad"

print(get_client_response(massage,CLIENT_API_URL))
