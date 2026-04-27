from fastapi.testclient import TestClient
from FastAPI_TicTacToe_Game_REST_API_Development_Project.main import app

client = TestClient(app)


def test_create_game():
    response = client.post("/games")
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_games():
    response = client.get("/games")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_game():
    create_response = client.post("/games")
    game_id = create_response.json()["id"]

    response = client.get(f"/games/{game_id}")
    assert response.status_code == 200
    assert response.json()["id"] == game_id


def test_game_not_found():
    response = client.get("/games/99999")
    assert response.status_code == 404


def test_make_move():
    create_response = client.post("/games")
    game_id = create_response.json()["id"]

    response = client.put(f"/games/{game_id}/move/1")
    assert response.status_code == 200


def test_invalid_move():
    create_response = client.post("/games")
    game_id = create_response.json()["id"]

    response = client.put(f"/games/{game_id}/move/10")
    assert response.status_code == 400