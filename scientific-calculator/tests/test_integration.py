from basic_operations import add
from advanced_operations import sine

def test_combined():
    result = add(10, sine(30))
    assert round(result, 1) == 10.5