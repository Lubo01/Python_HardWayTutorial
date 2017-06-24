# Exercise 6 Strings and Text

# formatting characters with % put values or variable values inside the string 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# we put variables into string through %s
y = "Those who know %s and those who %s." % (binary,do_not)

# alternative partial variables LL
y1 = "Those who know"
y2 = "and those who"
y3 = "."


print x
print y
# alternative with partial variables without % and formatting characters 
# connection with , = result with space, connection with + = result without space
print y1, binary, y2, do_not + y3

print "I said: %r." % x 
# single quotes mark a string (speech) inside a string 
print "I also said: '%s'." % y 

# boolean type of variable 
hilarious = True # or False (bool i.e. boolean type)
joke_evaluation = "Isn't that joke so funny?! %r"

# connection of 2 variables (different types: string + boolean) with %, instead of + (result without space)
# % makes conversion of boolean (or other variable type except string) into string for printing result 
print joke_evaluation % hilarious
# if we connect with + like: print joke_evaluation + hilarious
#, we get error that: cannot concatenate 'str' and 'bool' objects

w = "This is the left side of..."
e = "a string with a right side."

# connection of 2 variables (strings) with + (concatenate)(result without space)
print w + e 
# if we connect 2 strings with % (conversion) like: print w % e 
# , we get error that: not all arguments converted during string formatting

