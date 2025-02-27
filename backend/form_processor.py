from bs4 import BeautifulSoup


def get_form_field_descriptions(html_file_path):
    with open(html_file_path, "r") as file:
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
