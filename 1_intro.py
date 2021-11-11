# import FastAPI
from fastapi import FastAPI

app = FastAPI() # creating FastAPI instance

# creating a path operation
@app.get("/") # defining a path operation decorator
async def root(): # defining the path operation function
    return {"message": "Hello World"} # return the content

# Run the development server
# uvicorn 1_intro:app --reload

# Try opening:
# 1. http://127.0.0.1:8000/docs
# 2. http://127.0.0.1:8000/redoc

""" 
FastAPI generates a "schema" with all the API.

A schema is an abstract definition/description of something.
The schema definition includes API paths, parameters etc.


A path is commonly known as an 'endpoint' or 'route'. 
"""