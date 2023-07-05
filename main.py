#created my custom error in case of giving invalid inputs
class CustomError(ValueError):
    def __init__(self) -> str:
        super().__init__(f"Inputs are not valid since task was to add only numbers not strings!")


class addNumbers:
    def __init__(self):
        self.result=[]

    #main function
    def addNums(self,x,n):
        if isinstance(x,int) and isinstance(n,int):
            result = n + x
            self.result.append(result)
            return result
        else:
            raise CustomError()

    #getting last/recent result result
    def recent_result(self):
        return self.result

    #resetting last result
    def clean_result(self):
        self.result = []
        return 'Cleaned!'   
    

myClass=addNumbers()

print(myClass.addNums(55,4))
print(f'Recent result: {myClass.recent_result()}')

print(myClass.addNums(323,4))
print(f'Recent results: {myClass.recent_result()}')
print(f'History is {myClass.clean_result()}')





