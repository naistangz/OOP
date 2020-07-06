from student_data_inheritance import *

# Child class
class DevOps_student(Student):
    def __init__(self, name, ID, age, mood, grade, skillset):
        super().__init__(name, ID, age, grade, mood)
        self.skillset = skillset

    def add_skill(self, skill):
        self.skillset.append(skill)

    def say_hi(self):
        print("Name:", self.name,
              "\nID:", self.ID,
              "\nAge:",self.age,
              "\nMood:", self.mood,
              "\nGrade:", self.grade,
              "\nSkillset:", self.skillset)


Anais = Student("Anais", "1001", "23", "Happy", "100")
Anais.say_hi()
Saskia = Student("Saskia", 1020, 29, "Confused", 86)
Saskia.say_hi()

bob = DevOps_student("Bob", "1002", "30", "Energised", "95",['Python', 'AWS', 'SQL'])
bob.say_hi()
bob.add_skill("Javascript")
bob.add_skill("Databases")

Tina = DevOps_student("Tina", 1045, 45, "Motivated", 96, ['C++', 'Jenkins', 'Excel'])
Tina.say_hi()
Tina.add_skill("Java")
Tina.say_hi()