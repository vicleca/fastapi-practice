from exceptions import StoryException
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import article
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
	return JSONResponse(
		status_code=418,
		content={'detail': exc.name}
	)

models.Base.metadata.create_all(engine)
