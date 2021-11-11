from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item id": item_id}

# Value of path parameter item_id will be passed to the function
# argument item_id.

# Path Parameters with types
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int): # declaring the type of path parameter
    return {"item_id" : item_id}

# Try and observe:
# http://127.0.0.1:8000/items/3
# http://127.0.0.1:8000/items/foo
# http://127.0.0.1:8000/items/2.7

"""
    Predefined path parameters can be created using "Enum" class.
"""

from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

"""
    Creating a path inside a path
"""
# use, /files/{file_path: path}
# where, path = home/johndoe/file.txt

from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}