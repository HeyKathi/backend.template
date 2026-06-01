from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO
from datetime import datetime

from ..engine.database import get_db
from ..crud._crud import (
    create_game,
    get_games,
    get_game,
    make_move,
    export_games_to_xml
)

router = APIRouter()


@router.post("/games")
def create_new_game(db: Session = Depends(get_db)):

    return create_game(db)


@router.get("/games")
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


@router.get("/export/xml")
def export_xml(db: Session = Depends(get_db)):
    """
    Export all TicTacToe games as XML file.
    
    Returns:
        XML file download
    """
    try:
        xml_content = export_games_to_xml(db)
        
        # Create BytesIO object
        xml_bytes = BytesIO(xml_content.encode('utf-8'))
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"tictactoe-export_{timestamp}.xml"
        
        # Return as file download
        return StreamingResponse(
            iter([xml_bytes.getvalue()]),
            media_type="application/xml",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        raise HTTPException(500, f"Export failed: {str(e)}")