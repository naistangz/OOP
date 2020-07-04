from calculatorOOP.calculator import *

Calc = Simple_Calculator(num1, num2)

while True:
    def menu():
        options = """
        Please select one of the following: 
            ==================================
            + for addition
            - for subtraction 
            * for multiplication 
            / for division
            0 to Exit
            ==================================
            """
        print(options)
    menu()
    user_input = input("Enter operator: ")
    if user_input == "+":
        print(Calc.add())
    elif user_input == "-":
        print(Calc.sub())
    elif user_input == "*":
        print(Calc.multiply)
    elif user_input == "/":
        print(Calc.divide())
    elif user_input == "0":
        print("Goodbye! See you again soon!")
        break
    else:
        print("You have not typed in a valid operator, please run the program again.")



