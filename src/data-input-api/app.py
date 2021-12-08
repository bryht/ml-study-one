from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "title": "Welcome!" }

@app.post("/")
def create_data():
    return { "title": "Welcome1!" }