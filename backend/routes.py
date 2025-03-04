from fastapi import APIRouter
from services.form_processor import get_form_field_descriptions
from services.open_router_api import chat_with_openrouter
from services.pdf_processor import process_data
from config import LLM_MODEL_NAME

router = APIRouter()


@router.get("/get_tax_form_data")
async def get_tax_form_data():
    try:
        form_fields = get_form_field_descriptions(
            "../frontend/src/components/TaxForm.tsx"
        )
        db_vector = process_data("../data_samples")

        responses = []
        for field in form_fields:
            relevant_docs = db_vector.similarity_search(field["label"], k=3)
            context = "\n".join([doc.page_content for doc in relevant_docs])

            # prompt = (
            #     f"Extract the exact value for '{field['label']}' from the following context. "
            #     f"Provide ONLY the value itself. If the value is not found, respond with 'N/A'"
            #     f"Context:\n{context}"
            # )
            prompt = f"Based on the context, what is the '{field['label']}'? Provide only the required information for the field ID '{field['id']}'. Context: {context}"

            answer = chat_with_openrouter(
                model=LLM_MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
            )

            responses.append({**field, "response": answer.strip()})

        response_data = {field["id"]: field["response"] for field in responses}
        print(f"response_data: {response_data}")
        print("-" * 50)
        print(responses)
        return response_data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
