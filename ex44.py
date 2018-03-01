#Inheritance Versus Composition

"""Inheritance is used to indicate that one class will get most
 or all of its features from a parent class. This happens implicitly whenever
 you write class Foo(Bar), which says "Make a class Foo that inherits from Bar."
 When you do this, the language makes any action that you do on instances of Foo
 also work as if they were done to an instance of Bar. Doing this lets you put
 common functionality in the Bar class, then specialize that functionality
 in the Foo class as needed.
 
 When you are doing this kind of specialization, there are three ways
 that the parent and child classes can interact:

 1 Actions on the child imply an action on the parent.
 2 Actions on the child override the action on the parent.
 3 Actions on the child alter the action on the parent.
"""
 
# 1 Implicit Inheritance
 
class Parent (object):
 
	def implicit (self):
		print "PARENT implicit()"
		
class Child (Parent):

	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

	