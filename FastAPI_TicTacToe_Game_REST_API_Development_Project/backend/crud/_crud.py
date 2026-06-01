from sqlalchemy.orm import Session
from ..model._entity import Entity
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime


WIN = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]


def check_winner(board):

    for a,b,c in WIN:
        if board[a] != "-" and board[a] == board[b] == board[c]:
            return board[a]

    if "-" not in board:
        return "draw"

    return None


def create_game(db: Session):

    game = Entity()

    db.add(game)
    db.commit()
    db.refresh(game)

    return game


def get_games(db: Session):

    return db.query(Entity).all()


def get_game(db: Session, game_id: int):

    return db.query(Entity).get(game_id)


def make_move(db: Session, game_id: int, position: int):

    game = get_game(db, game_id)

    if not game:
        raise ValueError("Game not found")

    if position < 1 or position > 9:
        raise ValueError("Position must be between 1 and 9")

    board = list(game.board)

    if board[position-1] != "-":
        raise ValueError("Position already taken")

    board[position-1] = game.current_player

    board = "".join(board)

    winner = check_winner(board)

    game.board = board

    if winner == "draw":
        game.status = "draw"

    elif winner:
        game.status = f"{winner}_wins"

    else:
        game.current_player = "O" if game.current_player == "X" else "X"

    db.commit()
    db.refresh(game)

    return game


def export_games_to_xml(db: Session):
    """
    Export all TicTacToe games from the database as XML.
    
    Returns:
        str: XML string containing all games
    """
    games = get_games(db)
    
    # Create root element
    root = ET.Element('tictactoe_export')
    root.set('timestamp', datetime.now().isoformat())
    root.set('total_games', str(len(games)))
    
    # Add metadata
    metadata = ET.SubElement(root, 'metadata')
    ET.SubElement(metadata, 'export_date').text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ET.SubElement(metadata, 'application').text = 'TicTacToe REST API'
    ET.SubElement(metadata, 'version').text = '1.0'
    
    # Add games
    games_element = ET.SubElement(root, 'games')
    
    for game in games:
        game_elem = ET.SubElement(games_element, 'game')
        game_elem.set('id', str(game.id))
        
        # Game details
        ET.SubElement(game_elem, 'board').text = game.board
        ET.SubElement(game_elem, 'current_player').text = game.current_player
        ET.SubElement(game_elem, 'status').text = game.status
        
        # Board visualization (3x3 grid)
        board_visual = ET.SubElement(game_elem, 'board_visualization')
        board_chars = list(game.board)
        for row in range(3):
            row_elem = ET.SubElement(board_visual, 'row')
            row_elem.set('number', str(row + 1))
            for col in range(3):
                pos = row * 3 + col
                cell = ET.SubElement(row_elem, 'cell')
                cell.set('position', str(pos + 1))
                cell.set('column', str(col + 1))
                cell.text = board_chars[pos]
    
    # Pretty print the XML
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent='  ')
    # Remove the XML declaration and empty lines
    xml_lines = [line for line in xml_str.split('\n') if line.strip()]
    # Skip the first line (XML declaration) and return
    return '\n'.join(xml_lines[1:])