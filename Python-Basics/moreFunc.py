from BasicFunc import Calculator


class MoreFunc(Calculator):
    num2 = 200

    def __init__(self,c,d):
        Calculator.__init__(self,c,d)

    def getCompleteData(self):
        return self.num2 + self.num1 + self.sum()


obj = MoreFunc(2,10)
print(obj.getCompleteData())
