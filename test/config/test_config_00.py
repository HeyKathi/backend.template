import FastAPI_TicTacToe_Game_REST_API_Development_Project


def test_config_00() -> None:
    config = FastAPI_TicTacToe_Game_REST_API_Development_Project.config.Config.get_instance()
    assert config

    assert "sqlite:///:memory:" == config.connection_string
