from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from custom_log import log

from schemas import ProductBase

router = APIRouter(
    prefix='/templates',
    tags=['templates']
)

templates = Jinja2Templates(directory="templates")

@router.post("/products/{id}", response_class=HTMLResponse)
def read_item(id: str,
			  product: ProductBase,
			  request: Request,
			  bt: BackgroundTasks):
	
	bt.add_task(log_template_call, f"Template read for product with id {id}")

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

def log_template_call(message: str):
	log("MyAPI", message)
