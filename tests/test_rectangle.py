import pytest
from src.rectangle import Rectangle

@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area'),
     [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
    ids=[int, float]
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Area of rectangle with {side_a} and {side_b} should be {area}, actual is {r.area}'