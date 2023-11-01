from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter(
    prefix='/templates',
    tags=['tenolates']
)

templates = Jinja2Templates(directory="templates")

@router.get("/products/{id}", response_class=HTMLResponse)
def read_item(id: str, request: Request):
	return templates.TemplateResponse(
		"product.html",
		{
			"request": request,
			"id": id
		}
	)
