from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from .tutorial import app03, app04, app05

app = FastAPI()

app.include_router(app03, prefix='/chapter03', tags=['Chapter3 Request and Confirm'])
app.include_router(app04, prefix='/chapter04', tags=['Chapter4 '])
app.include_router(app05, prefix='/chapter05', tags=['Chapter5 '])


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get('/')
def hello_world():
    return {'hello': 'world'}


if __name__ == '__main__':
    uvicorn.run('run:app', host="175.24.205.189", port=8000, reload=True, workers=1)



