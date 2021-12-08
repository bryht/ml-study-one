from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return { "title": "Welcome!" }


class Item(BaseModel):
    timestamp : str
    humidity: float
    temperature: float
@app.post("/")
def create_item(item: Item):
    
    return item