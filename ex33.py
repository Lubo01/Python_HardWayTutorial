# Exercise 33: While Loops

# i = 0
# numbers = []

#while i < 6:
	# print "At the top i is %d" % i
	# numbers.append (i)
	
	# i = i + 1
	# print "Numbers now: ", numbers
	# print "At the bottom i is %d" % i
	
# print "The numbers: "

# for num in numbers:
	# print num
	
#If at any time that you are doing this it goes crazy (it probably will),
# just hold down CTRL and press c (CTRL-c) and the program will abort.
	
#variant with Loop converted into a Function:	
# def LoopFunction (maxValue, increment):
	# #x = raw_input ("Give me the number from 1 to 10:")
	# i = 0
	# numbers = []
	
	# while i < maxValue:
		# print "At the top i is %d" % i
		# numbers.append (i)
		
		# i = i + increment
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" % i	

	# print "The numbers: "

	# for num in numbers:
		# print num

# LoopFunction (21,2)

#variant with For Loop and range:

numbers = []

for i in range (0, 6):
	print "At the top i is %d" % i
	numbers.append (i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
	