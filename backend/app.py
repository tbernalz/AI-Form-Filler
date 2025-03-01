import requests
import json
from typing import Dict, List, Optional
from form_processor import get_form_field_descriptions
from ollama_api import chat_with_ollama


if __name__ == "__main__":
    try:
        form_fields = get_form_field_descriptions(
            "../frontend/src/components/TaxForm.tsx"
        )
        print(f"form_fields_ {form_fields}")

        responses = []
        for field in form_fields:
            prompt = f"Based on the document, what is the '{field['label']}'? Provide only the required information for the field ID '{field['id']}'."
            answer = chat_with_ollama(
                model="tinyllama", messages=[{"role": "user", "content": prompt}]
            )
            responses.append({**field, "response": answer})

        response_data = {field["id"]: field["response"] for field in responses}
        print(f"response_data: {response_data}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
