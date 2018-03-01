#Exercise 42: Is-A, Has-A, Objects, and Classes

##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
##Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		##Dog has-a name, attribute name set to name
		self.name = name

##Cat is-a Animal

	def __init__(self, name):
		##Cat has-a name, attribute name set to name
		self.name = name
		
##Person is-a object
class Person(object):

	def __init__(self, name):
		##Person has-a name
		self.name = name
		
		##Person has-a pet of some kind
		## "None" sets the deault value for a method self.pet
		self.pet = None
		
##Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		##function super takes __init__ function from superclass Person
		##super is the way how you can run the __init__ method of a parent class reliably
		super(Employee, self).__init__(name)
		##Employee has-a salary
		self.salary = salary

##Fish is-a object
class Fish(object):
	pass
	
##Salmon is-a Fish
class Salmon(Fish):
	pass
	
##Halibut is-a Fish
class Halibut(Fish):
	pass
	
##rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")

##mary is-a Person
mary = Person("Mary")

##mary has-a pet called Satan
mary.pet = satan

##frank is Employee and has-a salary
frank = Employee("Frank", 120000)

##frank has-a pet called rover
frank.pet = rover

##flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()	