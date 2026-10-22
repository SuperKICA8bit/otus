import pytest
from src.circle import Circle

@pytest.mark.xfail(reason='should fail because radius is zero')
def test_circle_zero_radius():
    assert Circle(radius=0)
