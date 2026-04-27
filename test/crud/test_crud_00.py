from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.crud import Crud
from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.engine.database import get_engine
from FastAPI_TicTacToe_Game_REST_API_Development_Project.backend.schema import EntityBase


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_01():
    return


def test_crud_02():
    return
