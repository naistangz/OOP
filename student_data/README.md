# Student Data :chart_with_upwards_trend:

This project adopts all 4 pillars of OOP 

**Criteria:**

* [Student_data.py](student_data.py) file as a parent class and [DevOps_student.py](DevOps_Student.py) as a child class
* Each [student_data.py](student_data.py) Must have at least 2 attributes and 2 methods
* Each [student_data.py](student_data_encapsulation.py) must have one public and private method and attribute
* [Student_data.py](student_data.py) must be imported in [Devops_student.py](DevOps_Student.py) to implement each oop pillar in their respective Repositories

`NOTE: ONLY ONE OOP PILLAR'S FUNCTIONALITY NEEDS TO BE ACHIEVED IN EACH REPO AS PER THEIR NAMES`

## Terminology 

**Name Mangling (also called name decoration)**
- Python provides private name mangling for class methods and attributes 
- It is used to prevent accidental internal attribute access
- 'Mangling' in python is used for 'private' class members by adding dunder prefixes.

```python
class Test(object):
    def __mangled_name(self):
        pass
    def normal_name(self):
        pass
t = Test()
>>> [attr for attr in dir(t) if 'name' in attr]
# Returns ['_Test__mangled_name', 'normal_name']          
```