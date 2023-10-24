import os
import requests
from typing import Dict

API_KEY = os.getenv("PLUTARCH_API_KEY")
BASE_URL = os.getenv("PLUTARCH_BASE_URL", "https://api.plutarch.ai")

if API_KEY is None:
    raise ValueError("The PLUTARCH_API_KEY environment variable is not set. Please go to https://www.plutarch.ai/dashboard to create one.")

class Chat:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def add_message(self, message: Dict[str, str]):
        response = requests.post(
            f"{BASE_URL}/chat/{self.chat_id}/messages",
            headers={"Authorization": API_KEY},
            json=message,
        )
        response.raise_for_status()

    def get_context(self, prompt: Dict[str, str]):
        response = requests.post(
            f"{BASE_URL}/chat/{self.chat_id}/get_context",
            headers={"Authorization": API_KEY},
            json=prompt,
        )
        response.raise_for_status()
        return response.json()
    
    def delete(self):
        response = requests.delete(
            f"{BASE_URL}/chat/{self.chat_id}",
            headers={"Authorization": API_KEY},
        )
        response.raise_for_status()

def create_chat():
    response = requests.post(
        f"{BASE_URL}/chat",
        headers={"Authorization": API_KEY},
    )
    response.raise_for_status()
    chat_id = response.json()["id"]
    return Chat(chat_id)