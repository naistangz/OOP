from calculator import *


Calc = Simple_Calculator(num1, num2)

while True:
    def menu():
        options = """
        Please select one of the following: 
            =======================================
            + for addition
            - for subtraction 
            * for multiplication 
            / for division
            % for modulus
            tr to find the area of a triangle
            in to convert cm_to_inches 
            cm to convert inches_to_cm 
            0 to exit
            ========================================
            """
        print(options)
    menu()
    user_input = input("Enter operator: ")
    if user_input == "+":
        print(Calc.add())
    elif user_input == "-":
        print(Calc.sub())
    elif user_input == "*":
        print(Calc.multiply())
    elif user_input == "/":
        print(Calc.divide())
    elif user_input == "%":
        print(Calc.modulo())
    elif user_input == "tr":
        print(Calc.area_triangle())
    elif user_input == "cm":
        print(Calc.cm_to_inches())
    elif user_input == "in":
        print(Calc.inches_to_cm())
    elif user_input == "0":
        print("Goodbye! See you again soon!")
        break
    else:
        print("You have not typed in a valid operator, please run the program again.")



