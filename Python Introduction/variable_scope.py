#  variable scope specifies the region where we can access a variable
#1. When we declare variables inside a function, 
# these variables will have a local scope (within the function). 
# We cannot access them outside the function.

#2.In Python, a variable declared outside of the function or in global scope is known as a global variable. 
# This means that a global variable can be accessed inside or outside of the function.

#3. In Python, nonlocal variables are used in nested functions whose local scope is not defined. 
# This means that the variable can be neither in the local nor the global scope.



# name ="Terry"# global scope(available inside and outside functions)

# def display_name():
#     name = "wanjiru" # local scope(available only inside this fuction)
#     print(name)

# display_name() 
# print(name)  
   
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
    