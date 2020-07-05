class Simple_Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
    def sub(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
    def multiply(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"
    def divide(self):
        return f"{self.num1}/{self.num2} = {self.num1 / self.num2}"
    def modulo(self):
        return f"{self.num1}%{self.num2} = {self.num1%self.num2}"

    def area_triangle(self):
        return f"The area of triangle is = {(self.num1/0.5)* self.num2}"

    def cm_to_inches(self):
        return f"{self.num1}cm to inches is = {self.num1/2.54}\n{self.num2}cm to inches is = {self.num2/2.54}"
    
    def inches_to_cm(self):
        return f"{self.num1} inches to cm is = {self.num1*2.54}\n{self.num2} inches to cm is ={self.num2*2.54}"

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
