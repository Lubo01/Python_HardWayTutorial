#Exercise 16: Reading and Writing Files

from sys import argv

script, filename = argv

# print "We're going to erase %r." % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."

# raw_input("?")

print "Opening the file..."
#open the file in write mode 'w' - this mode overwrites existing file
target = open (filename, 'w')	
#basic file modes to open:
# r	reading only
# w writing only, overwrites existing content
# a append, adds text to the end of file
# basic combinations:
# r+ enables writing at the beginning of the file
# w+ enables reading, but overwrites file with new content
# a+ enables reading

print "Truncating the file. Goodbye!"
#erase (empty) content of the file: open(filename,'w').truncate()
target.truncate()	

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")	#new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# #alternative more simple way with only one target.write command
# new_text = "%s\n%s\n%s\n" % (line1, line2, line3)
# target.write(new_text)

print "And finally, we close it."
target.close()
