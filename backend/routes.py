from fastapi import APIRouter
from services.get_tax_form_data import get_tax_form_data as fetch_tax_form_data

router = APIRouter()


@router.get("/get_tax_form_data")
async def get_tax_form_data():
    try:
        return fetch_tax_form_data()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
