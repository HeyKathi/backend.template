from fastapi import FastAPI

from .api._routes import router
from .engine.database import Base, engine

app = FastAPI(
    title="TicTacToe API",
    version="1.0"
)

# DB Tabellen erstellen
Base.metadata.create_all(bind=engine)

# Router einbinden
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.put("/text")
def store_text(text: str):
    global stored_text
    stored_text = text
    return {"status": "ok"}

@app.get("/text")
def get_text():
    return {"stored_text": stored_text}