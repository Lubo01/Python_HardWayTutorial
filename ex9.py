#Exercise 9 Printing Printing Printing

# Here's some new strange stuff, remember type it exactly.

#setting variable value 
days = "Mon Tue Wed Thu Fri Sat Sun"
#setting variable value with \n feature to set new Line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
#if we'd put %r to format variable, we get result w/o new lines just raw input
#example: print "Here are the months: %r" % months
#result: Here are the months: 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'

#three double quotes (without spaces) enable to put more text in between:
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

