from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from main import app
from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.api._routes import router
from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.engine.database import Base, engine, SessionLocal

app = FastAPI(
    title="TicTacToe API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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

