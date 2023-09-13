from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def calculate_value(
    request: Request,
    Group: str = Form(...),
    Ftu: float = Form(...),
    e: float = Form(...),
    t: float = Form(...),
    d: float = Form(...)
):
    result = Ftu * e * t * d  # Replace with your own formula
    return templates.TemplateResponse(
        "form.html", {"request": request, "result": result, "Group": Group, "Ftu": Ftu, "e": e, "t": t, "d": d}
    )
