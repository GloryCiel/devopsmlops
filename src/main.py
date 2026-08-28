from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


app = FastAPI(
    title = "FastAPI -Hello World code",
    description = "This is the Hello World of FastAPI.",
    version = "1.0.0",
)

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/")
def hello_world():
    return "FastApi World!!"

@app.get("/get_test/{input_val}")
def get_test1(input_val):
    return {"values": input_val}

@app.get("/get_test2/{input_val}")
def get_test2(input_val: int, q: str):
    return {"item_id": input_val, "q":q}

@app.post('/post_test')
def post_test(item: Item):
    return item

