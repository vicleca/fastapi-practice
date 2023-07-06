from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.get('/all')
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type='text/html')
