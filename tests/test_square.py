import pytest
from src.square import Square

@pytest.mark.smoke
def test_square_perimeter():
    assert Square(5).perimeter == 20
