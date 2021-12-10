from fastapi import FastAPI
from pymongo import MongoClient
from decouple import config
from bson.json_util import dumps

app = FastAPI()

@app.get("/")
def read_root():
    client = MongoClient(config('MONGODB_URL'))
    db = client.pico
    result=db.picodata.find({})
    return dumps(result)