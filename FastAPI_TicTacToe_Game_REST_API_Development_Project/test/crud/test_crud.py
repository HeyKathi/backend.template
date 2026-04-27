from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.crud._crud import check_winner


def test_check_winner_row():
    board = "XXX------"
    assert check_winner(board) == "X"


def test_check_winner_column():
    board = "X--X--X--"
    assert check_winner(board) == "X"


def test_check_winner_diagonal():
    board = "X---X---X"
    assert check_winner(board) == "X"


def test_draw():
    board = "XOXOOXXXO"
    assert check_winner(board) == "draw"


def test_no_winner():
    board = "XOX------"
    assert check_winner(board) is None