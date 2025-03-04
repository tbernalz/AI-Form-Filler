import requests
import json
from typing import Dict, List, Optional
from config import OLLAMA_API_URL


def chat_with_ollama(
    model: str,
    messages: List[Dict[str, str]],
    api_url: str = OLLAMA_API_URL,
    timeout: int = 30,
) -> Optional[str]:
    """
    Sends a chat message to the Ollama API and returns the response.

    Args:
        model (str): The name of the model to use (e.g., "deepseek-r1").
        messages (List[Dict[str, str]]): List of messages in the format:
            [{"role": "user", "content": "Your message here"}].
        api_url (str, optional): The URL of the Ollama API endpoint.
        timeout (int, optional): Timeout for the API request in seconds.

    Returns:
        Optional[str]: The concatenated response content from the model, or None if an error occurs.

    Raises:
        ValueError: If any message in the `messages` list is not a dictionary or lacks the required keys ("role" and "content").
        requests.exceptions.RequestException: If an error occurs during the API request.
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
        print(f"Error calling Ollama API: {e}")
        return None
