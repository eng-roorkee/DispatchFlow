import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_uber_access_token():
    url = "https://auth.uber.com/oauth/v2/token"
    payload = {
        "client_id": os.getenv("UBER_CLIENT_ID"),
        "client_secret": os.getenv("UBER_CLIENT_SECRET"),
        "grant_type": "client_credentials",
        "scope": "eats.deliveries"  # Adjust scope based on your developer access
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        print("🔑 Successfully generated a fresh Access Token!")
        return token_data.get("access_token")
    else:
        print(f"❌ Failed to retrieve token: {response.text}")
        return None

if __name__ == "__main__":
    access_token = get_uber_access_token()
    print(access_token)