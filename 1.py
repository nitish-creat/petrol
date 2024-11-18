class InputOutString(object):
    def getString(self,s):
        self.s = input()
    def printString(self):
        print(self.s.swapcase())