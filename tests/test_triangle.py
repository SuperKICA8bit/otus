import pytest
from src.triangle import Triangle

def test_triangle_area():

    triangle = Triangle(side_a = 2, side_b = 4, side_c = 5)
    assert triangle.area == 6

@pytest.mark.skip(reason='временно не тестировать')
def test_triangle_impos():
    with pytest.raises(ValueError, match="cannot be created with THOSE sides...."):
        Triangle(side_a = 1, side_b = 2, side_c = 10)