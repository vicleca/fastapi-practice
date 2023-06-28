from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all')
def get_all_blogs():
	return {'message': 'All blogs provided'}

class BlogType(str, Enum):
	short = 'short'
	story = 'story'
	howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
	return {'message': f'Blog type {type.value}'}

@app.get('/blog/{id}')
def get_blog(id: int):
	return {'message': f'Blog with id {id}'}
