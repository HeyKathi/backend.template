from fastapi import FastAPI
from ._routes import router
from engine.database import Base, engine


def create_app():

    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title="TicTacToe API",
        version="1.0"
    )

    app.include_router(router)

    return app