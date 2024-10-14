class Calculator:
    # class variables
    num1 = 100

    # default contructor
    def __init__(self, a, b):
        # instance variables
        self.firstNumber = a
        self.secondNumber = b

    def getData(self):
        print(self.firstNumber)
        print(self.secondNumber)

    def sum(self):
        return self.firstNumber + self.secondNumber + self.num1

    def diff(self):
        return self.firstNumber - self.secondNumber - self.num1

    def multi(self):
        return self.firstNumber * self.secondNumber

    def div(self):
        return self.firstNumber//self.secondNumber

# cl = Calculator(10, 20)
# print(cl.sum())
# print(cl.diff())
# print(cl.multi())
# print(cl.div())
# print(Calculator.num1)
# cl.getData()
