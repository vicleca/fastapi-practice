from fastapi import APIRouter
from typing import Optional
from fastapi import status, Response
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post('/new')
def create_blog():
	pass
