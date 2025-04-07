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
        response_data = response.json()

        if "error" in response_data:
            error_msg = response_data["error"].get("message", "Unknown API error")
            error_code = response_data["error"].get("code", "UNKNOWN")
            print(f"OpenRouter API Error {error_code}: {error_msg}")
            return None

        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            print("Unexpected response format:", response_data)
            return None

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error {e.response.status_code}: {e.response.text}")

    except Exception as e:
        print(f"Error calling OpenRouter API: {str(e)}")

    return None
