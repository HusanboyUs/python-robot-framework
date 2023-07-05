from main import CustomError,addNumbers
import pytest

test_class = addNumbers()

def test_numbers():
    assert test_class.addNums(45,15) == 60

def test_negatives():
    assert test_class.addNums(-40,5) == -35

def test_invalidInputs():
    with pytest.raises(CustomError):
        test_class.addNums('string',5)

def test_recent():
    add_new = test_class.addNums(23,5) #28 
    assert test_class.recent_result() == [60, -35, 28]
    add_new = test_class.addNums(50,23) #73
    assert test_class.recent_result() == [60, -35, 28,73] #hence we have added other numbers above
    

