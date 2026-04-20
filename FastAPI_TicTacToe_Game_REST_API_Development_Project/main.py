from fastapi import FastAPI, HTTPException

from .api._routes import router, game_detail, get_game, get_games
from .engine.database import Base, engine, SessionLocal

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

