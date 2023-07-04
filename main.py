#created my custom error in case of giving invalid inputs
class NotValidInputError(ValueError):
    def __init__(self,value,value2) -> str:
        super().__init__(f"Your input == {value} or {value2} is not valid, please check!")

class addNumbers:
    def addNums(x,n):
        if x or n <0:
            raise NotValidInputError(x,n)
        else:
            return x+n
    

print(addNumbers.addNums(-2,2))
