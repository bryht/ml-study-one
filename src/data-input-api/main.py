from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from pymongo import MongoClient
from decouple import config

app = FastAPI()

class Item(BaseModel):
    timestamp: str
    humidity: float
    temperature: float


@app.post("/")
def create_item(item: Item):
    client = MongoClient(config('MONGODB_URL'))
    db = client.pico
    db_item= {
        'time': item.timestamp,
        'humidity': item.humidity,
        'temperature': item.temperature
    }
    result=db.picodata.insert_one(db_item)
    return str(result.inserted_id)