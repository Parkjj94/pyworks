#1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val   #value = value + val
        return self.value

cal = Calculator()
print(cal.add(10))