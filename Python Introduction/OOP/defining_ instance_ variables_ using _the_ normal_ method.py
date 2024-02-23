# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):

		# Instance Variable
		self.breed = breed

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

# Explanation:

# In this example, We have defined a class named Dog and we have created a class variable animal. 
# We have created an instance variable breed in the constructor. The class Dog consists of two methods 
# setColor and getColor, they are used for creating and initializing an instance variable and retrieving the value of the instance variable. 
# We have made an object of the Dog class and we have set the instance variable value to brown and we are printing the value in the terminal.

