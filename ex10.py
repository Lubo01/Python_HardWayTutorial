# Exercise 10 What was that? Escape sequences (or "\" backslash)

#\t adds a horizontal tab into result
#\n adds a new line
#\\ escapes one \ and print the other \
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# triple quotes mark a string through more lines

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print "%r" % tabby_cat # %r i.e. what is raw input
print "%s" % tabby_cat # %s i.e. what you should see
print persian_cat
print backslash_cat
print fat_cat
