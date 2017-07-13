#Exercise 15: Reading Files

#write a sample file for reading:
#ex15_sample.txt with following text:
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

#we import argv from sys module
from sys import argv

#define argv, while argv converts filename into string
script, filename = argv
#set variable for opening the file with command open()
txt = open(filename)	#if opened directly in Python, put quotes: open("filename")

print "Here's your file %r:" % filename
#read the file content and print it to screen with command read()
print txt.read()	#works also directly as: print open(filename).read()
#close the opened file
open(filename).close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#----------------------
#alternative with raw_input:
rFileName = raw_input("What is the file name?")
print "Here's your file %r:" % rFileName
print open(rFileName).read()
open(rFileName).close






