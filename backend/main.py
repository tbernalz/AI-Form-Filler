from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("../frontend/src/components/TaxForm.tsx") as file:
        return HTMLResponse(content=file.read())
