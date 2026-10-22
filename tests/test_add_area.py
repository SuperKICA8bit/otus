import pytest
from src.rectangle import Rectangle
from src.square import Square

@pytest.mark.slow
def test_add_area():
    r = Rectangle(2,5)
    s = Square(2)
    total_area = r.add_area(s)

    assert total_area == 14