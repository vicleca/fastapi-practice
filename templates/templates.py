from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from schemas import ProductBase

router = APIRouter(
    prefix='/templates',
    tags=['tenolates']
)

templates = Jinja2Templates(directory="templates")

@router.post("/products/{id}", response_class=HTMLResponse)
def read_item(id: str, product: ProductBase, request: Request):
	return templates.TemplateResponse(
		"product.html",
		{
			"request": request,
			"id": id,
			"title": product.title,
			"description": product.description,
			"price": product.price,
		}
	)
