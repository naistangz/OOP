# Object Oriented Programming

OOP based projects covering Encapsulation, Inheritance, Polymorphism and Abstraction

# Project 1: [Basic Object Oriented Calculator	:abacus:](calculatorOOP)

``` bash
Phase 1: Build a simple calculator class containing add, subtract, multiply, divide.
Phase 2: Expand by creating:
Divisible by method that returns true or false dependent on the outcome
Work out and return the area of a triangle
inch to cm converter
NOTE -> Must be in class and method format
```

# Project 2: [DNA String Parsing :dna:](dnastring.py)

```
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:

20 12 17 21

NOTE -> Must be in class and method format
```

# Project 3: [Fizzbuzz :bulb:](fizzbuzz.py)

``` bash
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

NOTE -> Must be in class and method format
```

# Project 4: [Scrabble :books:](scrabble.py)

``` bash
Base Scrabble word calculator instructions
Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.

Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

```

# Project 5: [Student Data :chart_with_upwards_trend:](student_data)

**Project criteria:**
* [Student_data.py](student_data/student_data.py) file as a parent class and [DevOps_student.py](student_data/DevOps_Student.py) as a child class
* Each [student_data.py](student_data/student_data.py) Must have at least 2 attributes and 2 methods
* Each [student_data.py](student_data/student_data_encapsulation.py) must have one public and private method and attribute
* [Student_data.py](student_data/DevOps_Student.py) must be imported in devops_student.py to implement each oop pillar in their respective repositories

```bash
Student_data_inheritance
Student_data_encapsulation
Student_data_polymorphism
Student_data_abstraction
```


## The 4 pillars of OOP

## Inheritance 
- Inheritance is a way of creating a new class for using details of an **existing** class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class(or parent class).

Using Inheritance in Python
```python 
# parent class
class Animal:
    def __init__(self, eat, walk, hungry=True, mood): # Setting default value of hunger to True
        self.eat = eat
        self.walk = walk
        self.hungry = hungry
        self.mood = mood

# child class
class Bird(Animal):
    # using super(), (temporary object of the superclass) allows us to access methods of the base class (parent class)
    def __init__(self):
        super().__init__()
        print("I am a bird")

    def tweet(self):
        print("tweet tweet")

    def fly(self):
        print("I am a free bird")

pippa = Bird()
pippa.tweet()
```

In the above program, we created two classes i.e. `Animal` (parent class) and `Penguin` (child class). The child class inherits the functions of parent class. 

The child class modified the behaviour of the parent class. We also extended the functions of the parent class, by creating new methods like `tweet()` and `fly()`.

We used the `super()` function inside the `__init__()` method. This allows us to run the `__init__()` method of the parent class inside the child class. 

---

## Encapsulation 
- Concept of encapsulation is to keep together the implementation (code) and the data it manipulates (variables). 
- Python does not have the private keyword, unlike some other object oriented languages.
- In python, we can **restrict** access to methods and variables. This prevents data from being modified (encapsulation).
- In python, we denote private attributes using underscore `_` or dunder (double underscore) `__` as the prefix.

```python
class Robot(object):
    def __init__(self):
        self.a = 123
        self.b = 123
        self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
print(obj.__c)
```

**Outcome:**

```python
123
123
Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print(obj.__c)
AttributeError: 'Robot' object has no attribute '__c' 
```


`_` Single underscore denotes private variable. It should not be accessed directly. 

`__` Dunder or double underscore also denotes private variable. 

---

## Polymorphism
- Poly means many 
- Morph means change 
- Polymorphism refers to the ability of an object taking many forms. 
- Python being an OOP supports Polymorphism through Method overriding and operator overloading. 
- Polymorphism can be achieved through inheritance - Method overriding
- Method overriding provides ability to change the implementation of a method in a child class which is already defined in one of its super class or parent class. 
- If there is a method in a super class the method having the same name number of arguments in a child class is said to be **overriding** the parent class method. 
- We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name. 
- We can then later generalise calling these methods by disregarding the object we are working with. 

```python
## Example of class polymorphism and inheritance 
from math import pi

class Shape: 
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    
    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    
    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

class Circle(Shape):
    def __init__(self, radius):
        super().init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
```

**Output**

```bash
Circle
I am a two-dimenional shape.
Squares have each angle equal to 90 degrees.
153.93804002589985
```

Methods such as `__str__()`, which have not been overridden in the child classes, are used from the parent class. 

The `fact()` method for object `a(Square class)` is overridden. However, `fact()` method for object `b` has not been overridden. It is *inheriting* from the Parent `Shape` class. 

---

## Abstraction 
- Abstraction focuses on hiding the internal implementations of a process or method from the user. In this way, the user knows what he is doing but not how the work is being done. 
- Using a car as an analogy. We drive without knowing what is going on underneath. We use the breaks to stop the car but we don't know how the breaks work. 
- Another example is a TV set. We watch films without knowing the inner details of how TV works. 
- In Python, abstraction is achieved by using abstract classes and interfaces.

---

## Key Points to Remember:
- OOP makes the program easy to understand as well as efficient
- The class is shareable, therefore the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects (implement the same functionality), so programmers can write efficient code. 
- Encapsulation: only exposes selected information to the outside world. 
