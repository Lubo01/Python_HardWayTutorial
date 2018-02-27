#Exercise 21: Functions Can Return Something

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b	#return assigns the value to the variable which is calling the function 
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

#set variables through calling functions and setting arguments
#original numbers in arguments changed for result with purpose (20)
age = add(35, 5)
height = subtract(278, 48)
weight = multiply(25, 2)
iq = divide(10, 1)

#print variables values, which we get from return statement within a function above
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#set a variable with using multiple functions and calculating inside out 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#now, we use normal formula for "puzzle":
what2 = age + (height - (weight * (iq / 2)))
print what2

#now, we try simple formula:
what33 = (56 + 45) - (85 * (21 / 3))
print what33

#now, let's try simple formula to calculate through functions above:
what33F = subtract(add(56, 45), multiply(85, divide (21, 3)))
print what33F

#define my own Function
def MyFunction(arg1):
	print "\nConverting %d minutes to seconds:\n" % (arg1)
	return arg1 * 60
	
#get input by user (minutes for arg1)
#use float (decimal) or int (integer) for numbers
minutes = float(raw_input("\nHow many minutes do we convert?")) 

#call my Function
#seconds = MyFunction(minutes)
#print seconds
print MyFunction(minutes)

