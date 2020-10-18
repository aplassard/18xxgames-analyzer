import pytest
from xxanalyzer.game import Game

@pytest.fixture
def game_id_18ms():
    return "12886"

@pytest.fixture
def game_18ms(game_id_18ms):
    return Game(game_id_18ms)

def test_game_id_18ms(game_id_18ms):
    assert game_id_18ms == "12886"

def test_game_class(game_18ms):
    assert game_18ms.game_id == "12886"

def test_game_class_info(game_18ms):
    assert game_18ms.game_info
    assert game_18ms.game_info["id"] == 12886
    assert len(game_18ms.game_info["players"]) == 3
