from bs4 import BeautifulSoup
from typing import List, Dict


def get_form_field_descriptions(html_file_path: str) -> List[Dict[str, str]]:
    """
    Extracts descriptions of form fields (input, select, textarea) from an HTML file.

    This function parses the HTML file and retrieves information about form fields,
    including their associated labels, placeholders, names, and IDs. It returns a list
    of dictionaries, where each dictionary contains the label and ID of a form field.

    Args:
        html_file_path (str): The path to the HTML file to be parsed.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary contains:
            - "label": The label text associated with the form field (or placeholder/name if no label is found).
            - "id": The ID of the form field (or name if no ID is found).
    """
    try:
        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")

        form_fields = soup.find_all(["input", "select", "textarea"])

        field_info = []
        for field in form_fields:
            field_data = {}

            label = soup.find("label", {"for": field.get("id")})

            if label:
                field_data["label"] = label.get_text().strip().rstrip(":")
            else:
                placeholder = field.get("placeholder")
                name = field.get("name")
                field_data["label"] = placeholder or name

            field_id = field.get("id") or field.get("name")
            if field_id:
                field_data["id"] = field_id

            if "label" in field_data and "id" in field_data:
                field_info.append(field_data)

        return field_info

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{html_file_path}' was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while processing the HTML file: {e}")
