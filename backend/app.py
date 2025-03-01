from config import OLLAMA_MODEL
from form_processor import get_form_field_descriptions
from ollama_api import chat_with_ollama
from pdf_processor import process_data

if __name__ == "__main__":
    try:
        form_fields = get_form_field_descriptions(
            "../frontend/src/components/TaxForm.tsx"
        )
        db_vector = process_data("../data_samples")

        responses = []
        for field in form_fields:
            relevant_docs = db_vector.similarity_search(field["label"], k=3)
            context = "\n".join([doc.page_content for doc in relevant_docs])

            prompt = (
                f"Extract the exact value for '{field['label']}' from the following context. "
                f"Provide ONLY the value itself. If the value is not found, respond with 'N/A'"
                f"Context:\n{context}"
            )

            answer = chat_with_ollama(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )

            responses.append({**field, "response": answer.strip()})

        response_data = {field["id"]: field["response"] for field in responses}
        print(f"response_data: {response_data}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
