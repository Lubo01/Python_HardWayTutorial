#Exercise 13: Parameters, Unpacking, Variables

#import of feature argv (argument variable) from module sys
#Remember that modules give you features. Modules. Modules. Remember this.
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Run the script (file.py) as follows: 
#python ex13.py first 2nd 3rd	#we define 4 argument variables

##try
from sys import argv
script, cool = argv

# print "daddy",cool
# print script
print script
print cool

##try
from sys import argv
cool = raw_input("What's Your name?")
script, var = argv
print "File used: %s" % script
print "Number of usage:", var
print "User name:", cool


