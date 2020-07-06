# Abstraction is a simplified specification of an entity
# An abstraction is a representation of a computation entity
# Abstraction conceals its particular information and only gives the most relevant information to the programmer

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        print(f"{self.name} is {self.age} years old and achieved {self.grade} in the exam.")

    def grow(self):
        self.age += 1

    def getAge(self):
        print(self.age)

# Using only several lines of code to get something more elaborate
Anais = Student("Anais", 100, 23)
Anais.__repr__()
Anais.grow()
Anais.getAge()