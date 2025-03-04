from typing import List, Dict, Any
from langchain_community.vectorstores import FAISS
from services.open_router_api import chat_with_openrouter
from config import LLM_MODEL_NAME


def filling_form(
    form_fields: List[Dict[str, str]], db_vector: FAISS
) -> List[Dict[str, Any]]:
    """Processes form fields by retrieving relevant information using vector similarity search
    and querying an LLM for structured responses.

    Args:
        form_fields (List[Dict[str, str]]): A list of dictionaries containing form field metadata.
            Each dictionary should have at least the keys:
                - "id" (str): The field ID.
                - "label" (str): The field name or description.
        db_vector (FAISS): A FAISS vector store used for similarity searches to retrieve relevant documents.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary contains:
            - The original form field data.
            - A "response" key with the extracted answer from the LLM.
    """
    try:
        structured_responses = []
        for field in form_fields:
            relevant_docs = db_vector.similarity_search(field["label"], k=3)
            context = "\n".join([doc.page_content for doc in relevant_docs])

            prompt = (
                f"Extract the exact value for '{field['label']}' from the following context. "
                f"Provide ONLY the value itself. If the value is not found, respond with 'N/A'"
                f"Context:\n{context}"
            )

            answer = chat_with_openrouter(
                model=LLM_MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
            )

            structured_responses.append({**field, "response": answer.strip()})

        return structured_responses

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
