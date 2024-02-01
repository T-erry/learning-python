# str.format()- Optional method that gives users more control when displaying output
#{} this curly braces acts as a placeholder for our value

animal = "cow"
item = "moon"

#print ("The " + animal+ " jumped over the " +item)
#print ("The {} jumped over the {}".format("cow", "moon"))
#print ("The {0} jumped over the {1}".format(animal, item)) #positional arguments
# print ("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword arguments

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Terry"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name)) 
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) #left align
# print("Hello, my name is {:>10}. Nice to meet you".format(name))# right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name))# center align


#How to format numbers
pi = 3.14159
f_number = 1000
print("The number pi is {:.2f}".format(pi))
print("The number is {:,}".format(f_number))
print("The number is {:b}".format(f_number)) # binary represantation of our number
print("The number is {:0}".format(f_number))   # Octal represantation of our number
print("The number is {:X}".format(f_number))   # hexadecimal represantation of our number
