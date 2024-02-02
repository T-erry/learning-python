# exception = events detected during execution that interrupt the flow of a program
# The try...except block is used to handle exceptions in Python.
try:

        numerator = int(input("Enter a number to divide"))
        denominator = int(input("Enter a number to divide by: "))
        result = numerator/denominator
        print(result)
except ZeroDivisionError as e:
        print(e)
        print("You can't divide by zero!")
except ValueError as e:
        print(e)
        print("Enter only numbers!")
except Exception as e:
         print(e)
         print("something went wrong")
         
else:
        print(result)
finally:
        print("This will always excute")
        