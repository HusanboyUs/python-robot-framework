"""This  is a pytest script to check if main class (addNums) are woeking as expected"""

import pytest
from main import CustomError, AddNum


test_class = AddNum()



def test_numbers():
    '''This test function checks if the sum_of_integers function correctly computes
    the sum of two integers'''

    assert test_class.add_nums(45, 15) == 60


def test_negatives():
    '''This test function checks if the sum_of_integers function correctly computes
    the sum of two negatives integers'''
    assert test_class.add_nums(-40, 5) == -35


def test_invalid_inputs():
    '''This test function checks if the sum_of_integers function raises error when 
    it gets unsupported characters like string'''
    with pytest.raises(CustomError):
        test_class.add_nums('string', 5)


def test_recent():
    '''This test function checks if the sum_of_integers function correctly addes recent results 
    to history result and check if history result is correctly being returned with all 
    recent history'''
    first_calc = test_class.add_nums(23, 5)  # 28
    print(first_calc)
    assert test_class.recent_result() == [60, -35, 28]
    add_new = test_class.add_nums(50, 23)  # 73
    # hence we have added other numbers above
    print(add_new)
    assert test_class.recent_result() == [60, -35, 28, 73]
