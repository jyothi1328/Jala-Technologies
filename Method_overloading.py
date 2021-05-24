class Employee:
    def Hello_Emp(self,e_name=None):
        if e_name is not None:
            print("Hello "+e_name)
        else:
            print("Hello ")
            emp1=Employee()
            emp1.Hello_Emp()
            emp1.Hello_Emp("Besant")                                        



# Function to take multiple arguments
def add(datatype, *args):

	# if datatype is int
	# initialize answer as 0
	if datatype =='int':
		answer = 0
		
	# if datatype is str
	# initialize answer as ''
	if datatype =='str':
		answer =''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')
