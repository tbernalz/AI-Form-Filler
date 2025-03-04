import requests
from typing import Dict, List
from config import OPENROUTER_API_KEY, OPENROUTER_API_URL


def chat_with_openrouter(
    model: str,
    messages: List[Dict[str, str]],
) -> str:
    """
    Sends a chat message to the OpenRouter API and returns the response.

    Args:
        model (str): The model to use (e.g., "mistralai/mistral-7b-instruct").
        messages (List[Dict[str, str]]): List of messages in the format:
            [{"role": "user", "content": "Your message here"}].

    Returns:
        str: The response content from the model.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": messages,
    }

    try:
        response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error calling OpenRouter API: {e}")
        return None
