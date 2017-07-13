#Exercise 17: More Files

#more simple alternative

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()
open(to_file, 'w').write(indata)

print "Alright, all done."

open(from_file).close()
open(to_file).close()
