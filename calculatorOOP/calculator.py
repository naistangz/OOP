class Simple_Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
    def sub(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
    def multiply(self):
        return f"{self.num1}*{self.num2} = {self.num1 * self.num2}"
    def divide(self):
        return f"{self.num1}/{self.num2} = {self.num1 / self.num2}"

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
