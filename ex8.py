# Exercise 8 Printing Printing

# set a variable (string) with %r for formatting into raw format in result
formatter = "%r %r %r %r"

#conversion of various types of data (numbers, strings,booleans and variables)
#conversion includes formatting with %r into raw result 
#%r: String (converts any python object using repr()).
print formatter % (1, 2, 3, 4) #format numbers, with space, without commas
print formatter % ("one", "two", "three", "four") #format str with single quotes
print formatter % (True, False, False, True) #format bool 
print formatter % (formatter, formatter, formatter, formatter) #print var as str

#text in more rows for better code reading. result in one row connected by ","
#str formatted into single quotes by default,
#doublequotes used when single quote inside str
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)



