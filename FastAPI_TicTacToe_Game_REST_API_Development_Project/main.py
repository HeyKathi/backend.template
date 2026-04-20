from fastapi import FastAPI

app = FastAPI()

# Variable to store text
stored_text = ""

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

@app.put("/text")
def store_text(text: str):
    global stored_text
    stored_text = text
    return "ok"

@app.get("/text")
def get_text():
    return stored_text