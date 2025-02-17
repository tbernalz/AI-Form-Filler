import requests
import json
from typing import Dict, List, Optional


def chat_with_ollama(
    model: str,
    messages: List[Dict[str, str]],
    api_url: str = "http://localhost:11434/api/chat",
    timeout: int = 30,
) -> Optional[str]:
    """
    Sends a chat message to the Ollama API and returns the response.

    Args:
        model (str): The model to use (e.g., "deepseek-r1").
        messages (List[Dict[str, str]]): List of messages in the format:
            [{"role": "user", "content": "Your message here"}].
        api_url (str): The URL of the Ollama API endpoint.
        timeout (int): Timeout for the API request in seconds.

    Returns:
        Optional[str]: The response content from the model, or None if an error occurs.
    """
    for message in messages:
        if (
            not isinstance(message, dict)
            or "role" not in message
            or "content" not in message
        ):
            raise ValueError(
                "Each message must be a dictionary with 'role' and 'content' keys."
            )

    payload = {
        "model": model,
        "messages": messages,
    }

    headers = {
        "Content-Type": "application/json",
    }
    try:
        full_response = ""
        with requests.post(
            api_url, json=payload, headers=headers, timeout=timeout, stream=True
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    content = chunk.get("message", {}).get("content", "")
                    full_response += content
        return full_response.strip()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the Ollama API: {e}")
        return None


if __name__ == "__main__":
    messages = [
        {
            "role": "user",
            "content": "How to prepare for a marathon",
        }
    ]
    try:
        response = chat_with_ollama(model="tinyllama", messages=messages)
        if response:
            print("Model response:\n", response)
        else:
            print("Failed to get a response from the model.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
