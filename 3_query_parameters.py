"""
    Query parameters are function parameters that are not a part of
    the path parameters.
"""

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]

"""
    Query is the set of key-value pairs that go after "?" in a URL
    separated by "&"

    URL for above function will look like,
    http://127.0.0.1:8000/?skip=0&limit=10
"""
# Optional query parameters can be declared by setting their default
# to None
######################################################################################################
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
######################################################################################################
"""
    Multiple path and query parameters can be declared  at the same time
    without any specific order.
"""

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, 
    item_id: str, 
    q:Optional[str]=None, 
    short:bool=False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description."}
        )
    return item
######################################################################################################
"""
    A default value cannot be declared for a non-optional query parameter.
"""
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    item_id: str, # path parameter
    needy: str, # non-optional query parameter
    skip: int=0, # query parameter
    limit: Optional[int]=None # optional query parameter
    ):
    item = {
        "item_id": item_id, 
        "needy":needy,
        "skip": skip,
        "limit": limit
    }
    return item
# Query parameter "needy" is a required query parameter of type str.
