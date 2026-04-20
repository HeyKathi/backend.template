from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..engine.database import get_db
from ..crud._crud import (
    create_game,
    get_games,
    get_game,
    make_move
)

router = APIRouter()


@router.post("/games")
def create_new_game(db: Session = Depends(get_db)):

    return create_game(db)


@router.get("/allgames")
def list_games(db: Session = Depends(get_db)):

    return get_games(db)


@router.get("/games/{game_id}")
def game_detail(game_id: int, db: Session = Depends(get_db)):

    game = get_game(db, game_id)

    if not game:
        raise HTTPException(404, "Game not found")

    return game


@router.put("/games/{game_id}/move/{position}")
def move(game_id: int, position: int, db: Session = Depends(get_db)):

    try:
        return make_move(db, game_id, position)
    except ValueError as e:
        raise HTTPException(400, str(e))