from sqlalchemy.orm import Session
from model._entity import Entity


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