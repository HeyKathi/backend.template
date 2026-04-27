from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .backend.api._routes import router, game_detail, get_game, get_games
from .backend.engine.database import Base, engine, SessionLocal

app = FastAPI(
    title="TicTacToe API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Tabellen erstellen
Base.metadata.create_all(bind=engine)

# Router einbinden
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

