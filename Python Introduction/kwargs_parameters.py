# **kwargs - parameters that will pack all arguments into a dictionary
            # useful so that a function can accept a varying amount of keyword arguments

def hello(**data):
    
    for key, value in data.items():
        print("{} is {}" .format(key, value))

hello(first="Terry", middle ="Ann", last="Wanjiru", age= 24)    