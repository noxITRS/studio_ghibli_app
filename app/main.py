from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

EXTERNAL_API_URL = "https://ghibliapi.herokuapp.com/films/"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    response = requests.get(EXTERNAL_API_URL)
    films = response.json()
    return templates.TemplateResponse(
        "index.html", {"request": request, "films": films}
    )


@app.get("/films/{film_id}")
def film_detail_view(request: Request, film_id: str):
    response = requests.get(EXTERNAL_API_URL + film_id)
    film = response.json()
    # if "title" not in film:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse(
        "film_detail.html", {"request": request, "film": film}
    )
