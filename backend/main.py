from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from routes import router as api_router, get_tax_form_data

app = FastAPI()
app.include_router(api_router)


@app.post("/auto-fill-form")
async def auto_fill_form():
    try:
        print("Auto-filling form...")
        auto_filled_data = await get_tax_form_data()
        print(auto_filled_data)

        return JSONResponse(content=auto_filled_data, status_code=200)
    except Exception as e:
        print.error(f"Error in auto-fill form: {e}")
        raise HTTPException(status_code=500, detail="Failed to auto-fill form")
