import sys
"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number
For multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

NOTE -> Must be in class and method format
"""

# class Fizzy:
def fizzbuzz():
    try:
        n = int(input("Please select a number between 1 and 100: \n"))
    except ValueError:
        print("The input was not a valid integer. Please select a number:")
        sys.exit(0)
    if n % 3 == 0 and n % 5 == 0:
        return f"The you have selected is: {n}\nThe outcome is: fizzbuzz"
    elif n % 3 == 0:
        return f"The you have selected is: {n}\nThe outcome is: fizz"
    elif n % 5 == 0:
        return f"The number you have selected is: {n}\nThe outcome is: buzz"
    else:
        return f"The number you have selected is: {n}\nIt is neither divisible by 3 nor 5"


    #
    # try:
    #     n = int(input("Please select a number between 1 and 100: \n"))
    #     # n = int(n)
    # except ValueError:
    #     print("The input was not a valid integer. Please select a number.")

print(fizzbuzz())