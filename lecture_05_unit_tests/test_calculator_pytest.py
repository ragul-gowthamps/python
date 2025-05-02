from calculator import square 


#you can run this test using pytest by running the command `pytest test_calculator_pytest.py` in the terminal.
# pytest will automatically discover the test functions and run them. 
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():    
    assert square(0) == 0
    
import pytest    
def test_str():
    with pytest.raises(TypeError):
        square("string")

