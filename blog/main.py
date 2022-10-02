from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas
app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request
    return {'title': request.title, 'body': request.body}
