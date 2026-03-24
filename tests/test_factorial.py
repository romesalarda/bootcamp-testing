import pytest
from mymath.factorial import factorial

def test_3():

    
    assert factorial(3) == 6

def test_5():
    assert factorial(5) == 120

def test_4():
    assert factorial(4) == 24

def test_42():
    assert factorial(42) == 1405006117752879898543142606244511569936384000000000

def test_negative():
    with pytest.raises(ValueError) as excinfo:
        factorial(-1)
        