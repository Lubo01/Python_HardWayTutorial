#Exercise 11  Asking Questions, Input Data

#questions aimed to get input data from user:
print "How old are you?",	#comma prevents making new line for the answer
age = raw_input()	
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
#raw_input is better than just input
#input() function will try to convert things entered as if they were Python code,
# but it has security problems so you should avoid it.

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#additional questions LL:
print "What's your name?",
name = raw_input()
print "What's your surname?",
surname = raw_input()

print "User name is:", name, surname

#usage of input directly in active python:
#a = raw_input('->') "prompt used in form of ->"
#a gives result: data as inputed by user

print "Cash counting:"
print "How many 10 cents do you have?",
a10cent = int(raw_input())
print "How many 50 cents do you have?",
a50cent = int(raw_input())
print "How many 1 euros do you have?",
a1eur = int(raw_input())
print "How many 5 euros do you have?",
a5eur = int(raw_input())
cash = a10cent * 0.1 + a50cent * 0.5 + a1eur * 1 + a5eur * 5
print "The cash amounts to", cash, "euros."