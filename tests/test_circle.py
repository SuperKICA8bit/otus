import math
import pytest
from src.circle import Circle

@pytest.mark.parametrize("radius, area", [(1,math.pi), (2, 4* math.pi)])
def test_circle_area(radius, area):
    assert Circle(radius).area == area

def test_circle_zero_radius():
    with pytest.raises(ValueError):
        Circle(radius=0)
