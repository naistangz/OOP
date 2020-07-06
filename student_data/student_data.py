# Parent class

class Student:
    def __init__(self, name, ID, age, mood, grade):
        self.name = name
        self.ID = ID
        self.age = age
        self.mood = mood
        self.grade = grade

    def say_hi(self):
        print("Name:", self.name,
                "\nID:", self.ID,
                "\nAge:", self.age,
                "\nMood:", self.mood,
                "\nGrade:", self.grade)









