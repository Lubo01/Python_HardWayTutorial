#Exercise 29: What If (If statement)

"""
#If statement creates what is called a "branch" in the code. It creates more branches 
i.e. more ways which code will be executed based upon boolean result of the statement.

#If statement tells your script, "If this boolean expression is True, then run
the code under it, otherwise skip it."

#A colon (:) at the end of a line is how you tell Python you are going to create
a new "block" of code, and then indenting four spaces tells Python what lines
of code are in that block.
"""

people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5	#+= as increment by operator

	
if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."

