class Validate:
    def isEven(self, num):
        if num % 2 == 0:
            return True
        else:
            return False

    def isInt(self, num):
        if type(num) == int:
            return True
        else: 
            return False

    def isStr(self, num):
        if type(num) == str:
            return True
        else: 
            return False

    def isInput(self, input, valid_choices):
        if input in valid_choices:
            return True
        else: 
            return False
