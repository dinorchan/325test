from enum import Enum

from fastapi import APIRouter

app03 = APIRouter()

@app03.get('/path/parameters')
def path_params01():
    return {"msg": "This is a message"}


@app03.get('/path/{parameters}')
def path_params01(parameters: str):
    return {"msg": parameters}

class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"


@app03.get("/enum/{city}")
async def lastest(city: CityName):
    if city == CityName.Shanghai:
        return {"city_name": city, "confirmed": 1492, "death": 7}
    if city == CityName.Beijing:
        return {"city_name": city, "confirmed": 971, "death": 9}
    return {"city_name": city, "lastest": "unknown"}


@app03.get('/files/{file_path:path}') # file_path中出现'/'作为str处理
def filepath(file_path: str):
    return f"the file path is {file_path}"



