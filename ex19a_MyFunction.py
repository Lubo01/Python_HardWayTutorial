#My Function Test

#define a function for speed measurement:
def Your_speed(distance, time):
	print "\n\t If you traveled %d km as long as %d hours," % (distance, time),
	print "\n\t then your speed was %d km/h." % (distance / time)

#Let's get the values from user:
print "What about counting the speed of your travelling?\n"
travelled_km = float(raw_input("Tell me, please, how many km did you travel?"))
travelled_hours = float(raw_input("And now, tell me, please, how many hours did you travel?"))
	
#Let's call my function:
Your_speed(travelled_km, travelled_hours)
