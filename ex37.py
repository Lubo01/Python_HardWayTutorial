#Exercise 37: Symbol Review - Python Basic Keywords

#Keywords

and			#logical and
assert		#testing method, a variant of check 
			e.g. assertEqual(a,b)	check that a==b 
			e.g. assertTrue (x)		check that bool(x) is True
break		#stops the loop
class		#define a class, e.g. class name(object)
continue	#don't process further the loop, continue with next iteration now
def			#define a function
del			#delete from a dictionary
except		#handle exceptions
exec		#run string as Python / execute
			e.g. exec 'print "Hello"'
finally		#part of command try: Exceptions or not, finally do this no matter what.
for			#loop (actually: for each)
global		# 	Declare that you want a global variable.
if...elif...else	#if statement
import...from	#import modules, or import specific part of modules (...from...)
is			#like == to test equality, e.g. 1 is 1 == True
lambda		#Create a short anonymous function. One way to write small functions
			is to use the lambda statement. lambda takes a number of parameters
			and an expression combining these parameters, and creates a small
			function that returns the value of the expression:
			e.g. lowercase = lambda x: x.lower()
not			#logical not
or			#logical or
pass		#this block is empty
			e.g. def empty(): pass
print		#print this string '...'
raise		#Raise an exception when things go wrong.
			e.g. raise ValueError("No")
return		#Exit the function with a return value.
try			#Try this block, and if exception, go to except.
while		#while loop
with-as statement	#With an expression as a variable do.
					provide reference to other part of the code as object
					e.g. class controlled_execution:...some code to reuse often,
						 use through functions...
						 e.g. def __enter__(self):
						set things up
						return thing
					with controlled_execution() as thing:
					some code
					
					other example e.g.
					with open("x.txt") as f:
					data = f.read()
					do something with data
yield		#Pause here and return to caller.
			e.g.def X(): yield Y; X().next()
		
#Data Types

True 		#True boolean value. 	True or False == True
False 		#False boolean value. 	False and True == False
None 		#Represents "nothing" or "no value". 	x = None
strings 	#Stores textual information. 	x = "hello"
numbers 	#Stores integers. 	i = 100
floats 		#Stores decimals. 	i = 10.389
lists 		#Stores a list of things. 	j = [1,2,3,4]
dicts (dictionaries)	#Stores a key=value mapping of things. 	e = {'x': 1, 'y': 2}

#String Escape Sequences

Escape 	Description
\\ 		Backslash
\' 		Single-quote
\" 		Double-quote
\a 		Bell
\b 		Backspace
\f 		Formfeed
\n 		Newline
\r 		Carriage
\t 		Tab
\v 		Vertical tab

#String Formats

Escape 	Description 	Example
%d 	Decimal integers (not floating point). 	"%d" % 45 == '45'
%i 	Same as %d. 	"%i" % 45 == '45'
%o 	Octal number. 	"%o" % 1000 == '1750'
%u 	Unsigned decimal. 	"%u" % -1000 == '-1000'
%x 	Hexadecimal lowercase. 	"%x" % 1000 == '3e8'
%X 	Hexadecimal uppercase. 	"%X" % 1000 == '3E8'
%e 	Exponential notation, lowercase 'e'. 	"%e" % 1000 == '1.000000e+03'
%E 	Exponential notation, uppercase 'E'. 	"%E" % 1000 == '1.000000E+03'
%f 	Floating point real number. 	"%f" % 10.34 == '10.340000'
%F 	Same as %f. 	"%F" % 10.34 == '10.340000'
%g 	Either %f or %e, whichever is shorter. 	"%g" % 10.34 == '10.34'
%G 	Same as %g but uppercase. 	"%G" % 10.34 == '10.34'
%c 	Character format. 	"%c" % 34 == '"'
%r 	Repr format (debugging format). 	"%r" % int == "<type 'int'>"
%s 	String format. 	"%s there" % 'hi' == 'hi there'
%% 	A percent sign. 	"%g%%" % 10.34 == '10.34%'

#Operators

Operator 	Description 	Example
+ 	Addition 	2 + 4 == 6
- 	Subtraction 	2 - 4 == -2
* 	Multiplication 	2 * 4 == 8
** 	Power of 	2 ** 4 == 16
/ 	Division 	2 / 4.0 == 0.5
// 	Floor division 	2 // 4.0 == 0.0
% 	String interpolate or modulus 	2 % 4 == 2
< 	Less than 	4 < 4 == False
> 	Greater than 	4 > 4 == False
<= 	Less than equal 	4 <= 4 == True
>= 	Greater than equal 	4 >= 4 == True
== 	Equal 	4 == 5 == False
!= 	Not equal 	4 != 5 == True
<> 	Not equal 	4 <> 5 == True
( ) 	Parenthesis 	len('hi') == 2
[ ] 	List brackets 	[1,3,4]
{ } 	Dict curly braces 	{'x': 5, 'y': 10}
@ 	At (decorators) 	@classmethod
, 	Comma 	range(0, 10)
: 	Colon 	def X():
. 	Dot 	self.x = 10
= 	Assign equal 	x = 10
; 	semi-colon 	print "hi"; print "there"
+= 	Add and assign 	x = 1; x += 2
-= 	Subtract and assign 	x = 1; x -= 2
*= 	Multiply and assign 	x = 1; x *= 2
/= 	Divide and assign 	x = 1; x /= 2
//= 	Floor divide and assign 	x = 1; x //= 2
%= 	Modulus assign 	x = 1; x %= 2
**= 	Power assign 	x = 1; x **= 2