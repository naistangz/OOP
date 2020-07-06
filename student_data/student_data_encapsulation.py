# Encapsulation

class Student:
    def __init__(self, name, ID, age, mood, grade, salary):
        self.name = name
        self.ID = ID
        self.age = age
        self.mood = mood
        self.grade = grade
        self.__salary = salary # private attribute

    def say_hi(self):
        print("Name:", self.name,
                "\nID:", self.ID,
                "\nAge:", self.age,
                "\nMood:", self.mood,
                "\nGrade:", self.grade)

    def mood(self):
        print("I am feeling:", self.mood)

    def __salary(self):
        print(f"My salary expectations is: {self.__salary}")

s1 = Student("Chris", 1001, 56, "Satisfied", 45, 50000)
s1.say_hi()
# 'Student' object has no attribute 'Salary'
# self.__salary is hidden

# Accessing private attributes with name mangling
# Name mangling process helps to access the class variables from outside the class
# Using a dunder prefix for a class object will 'mangle' or destroy the attribute, and modified
# Every attribute with double underscore will be changed to _object._class_variable
# Practice should be refrained

print(f"Salary expectations:{s1._Student__salary}")
# Prints Salary expectations: 50,000

