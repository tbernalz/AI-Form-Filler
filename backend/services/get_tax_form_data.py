from services.form_processor import get_form_field_descriptions
from services.filling_form import filling_form
from services.pdf_processor import process_data


def get_tax_form_data():
    try:
        form_fields = get_form_field_descriptions(
            "../frontend/src/components/TaxForm.tsx"
        )
        db_vector = process_data("../data_samples")
        structured_responses = filling_form(form_fields, db_vector)
        response_data = {
            field["id"]: field["response"] for field in structured_responses
        }

        return response_data

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
