import pytest
import 18

@pytest.fixture
def game_id_18ms():
    return "12886"

def test_get_game(game_id_18ms):
    assert game_id_18ms == "12886"