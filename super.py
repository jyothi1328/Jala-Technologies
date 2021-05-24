'''
# Python program to demonstrate
# super function


class Animals:
	
	# Initializing constructor
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	
	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
	
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
	
class Dogs(Animals):
	def __init__(self):
		super().__init__()

	def isMammal(self):
		super().isMammal()

class Horses(Animals):
	def __init__(self):
		super().__init__()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")

# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
'''


#Call constructor of the parent class using super()

# this is the class which will become
# the super class of "Subclass" class
class Class():
	def __init__(self, x):
		print(x)

# this is the subclass of class "Class"
class SubClass(Class):
	def __init__(self, x):

		# this is how we call super
		# class's constructor
		super().__init__(x)

# driver code
x = [1, 2, 3, 4, 5]
a = SubClass(x)


