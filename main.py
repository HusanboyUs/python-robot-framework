"""This is main task file which coder should write a script
a class to add integers and return the result"""


class CustomError(ValueError):
    '''CustomError: Raised when the user provides non-integer input
    Examples:
        >>> raise CustomError("Invalid input! Only integers are allowed.")
        CustomError: Invalid input! Only integers are allowed.
    '''

    def __init__(self) -> str:
        super().__init__("Inputs are not valid since task was to add only numbers not strings!")


class AddNum:
    '''Main task class to add two numbers

    Methods:
        add_nums(x, n):
            Takes two integer arguments (x and n) and returns the sum of the two integers.
            It also updates the result history with the computed sum.
        
        recent_result():
            Returns the list of recent results, representing the history of computed sums.
        
        clean_result():
            Resets the result history by clearing the list of computed sums.
    '''

    def __init__(self):
        self.result = []

    # main function
    def add_nums(self, val, val2):
        '''Takes two arguments (integers) and returns sum of the both integers'''
        if isinstance(val, int) and isinstance(val2, int):
            result = val + val2
            self.result.append(result)
            return result
        raise CustomError()

    # getting last/recent result result
    def recent_result(self):
        '''Returns recent results of sums of integers'''
        return self.result

    # resetting last result
    def clean_result(self):
        '''Cleans history result'''
        self.result = []
        return 'Cleaned!'


myClass = AddNum()

print(myClass.add_nums(10, 4))
print(f'Recent result: {myClass.recent_result()}')


print(myClass.add_nums(323, 4))
print(f'Recent results: {myClass.recent_result()}')
print(f'History is {myClass.clean_result()}')
