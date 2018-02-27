#Exercise 20: Functions and Files

from sys import argv

script, input_file = argv

#define a function
def print_all(f):
	print f.read()	#read file
	
#define a function	
def rewind(f):
	f.seek(0)	#seek the beginning of the file, the byte 0 (zero)
	
#define a function	
def print_a_line(line_count, f):
	print line_count, f.readline()	#read one line from the file, specify the line number

#set variable for opening a file from argv
current_file = open(input_file)

print "First let's print the whole file:\n"
#call a function
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#call a function
rewind(current_file)

print "Let's print three lines:"

#set variable
current_line = 1	#current line = 1
#call a function
#we assign current_line to argument line_count and current_file to argument f
print_a_line(current_line, current_file)

# current_line = current_line +1	#current line = 2
current_line +=1	#shorter alternative for increment of variable current_line
print_a_line(current_line, current_file)

#current_line = current_line + 1	#current line = 3
current_line +=1
print_a_line(current_line, current_file)
