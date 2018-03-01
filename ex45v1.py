#Make your own game

#basic description - game idea
"""
Car Competition
there are 3 cars Skoda, Nissan and Audi competing in tournament consisting
of 5 races. You need to choose your car and throw dice to compete.
You can also bet each race which car wins.
For each race there are points distributed based on highest rank of dice points:
5 points for winner, 3 points for 2nd runner and 2 points for loser.
Sum of points at the end of tournament determines ranking of cars.

"""
#1 start with Design
#2 basic game concept in version 1

from sys import exit
from random import randint

#Game Engine to play 
class Engine (object):

	def __init__(self,race):
		self.race = race
	def play (self):
		#self.race.result()
		#print resultTable
		
		"""
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()		
		"""
#Race class for 5 Races with description and dice rolling
class Race (object):

	def __init__(self):
		pass
	
	#iter method makes an object iterable, i.e. can make next object instance
	#(needed for use of sorted function or for loop)	
	def __iter__ (self):
		return iter(self.list)
	
	def result (score):
		resultTable = sorted(score, key=lambda x: x[1], reverse = True)
		
		#check what-if 2 or 3 cars roll the same points of dice		
		if resultTable [0][1] > resultTable [1][1]:
			winner = resultTable [0][0]
		elif resultTable [1][1] > resultTable [2][1]:
			winner = "%s and %s" % (resultTable [0][0],resultTable [1][0])
		else:
			winner = "All racers won within the same time!!!"
		
		#print "\n Score: ", score
		#print "\n Result Table:", resultTable
		print "\n\n The winner is:\t %s \n" % winner
		
		print "\n Result table:\n "
		print "\t", resultTable [0][0], ":", resultTable [0][1]
		print "\t", resultTable [1][0], ":", resultTable [1][1]
		print "\t", resultTable [2][0], ":", resultTable [2][1], "\n\n"
		
	cars = ["Skoda", "Nissan", "Audi"]
	carSpelling = ["Skoda","skoda","s","Nissan","nissan","n","Audi","audi","a"]
	correct = 0
	
	print "\n Get ready, game is starting..."
	print "\n This is new car tournament. There are 3 cars racing:\n"
	print "\n".join(cars)
	
	while correct < 1:
		playerChoice = raw_input ("Choose your car:")
	
		if playerChoice in carSpelling:
			correct = 1
		else:
			print "Misspelled. Please, type the car name correctly."
	
	if playerChoice in carSpelling[0:3]:
		playerCar = "Skoda"
		print playerCar
	elif playerChoice in carSpelling[3:6]:
		playerCar = "Nissan"
	elif playerChoice in carSpelling[6:9]:
		playerCar = "Audi"
	
	print "\n OK. so you will race with %s \n" % (playerCar)
	print "Let`s start the game:\n"
			
	raw_input ("Roll the dice: (hit 'Enter' or press any key)")
	
	SkodaDice = randint(1,6)
	NissanDice = randint(1,6)
	AudiDice = randint(1,6)
	
	if playerCar == "Skoda":
		playerDice = SkodaDice
	elif playerCar == "Nissan":
		playerDice = NissanDice
	elif playerCar == "Audi":
		playerDice = AudiDice
	else: print "Something went wrong?"
	
	print "\n You have got %s!\n" % playerDice
		
	score = [["Skoda ", SkodaDice],["Nissan", NissanDice],["Audi  ", AudiDice]]
		
	max_sub = max(score, key=lambda x: x[1])
	max_val = max_sub[1]
	max_index = max_sub[0]
	#print max_sub
	#print max_val, max_index
			
	raw_input ("Who wins? (hit 'Enter' or press any key)")
	
	print "\n The winner got", max_val
	"""
	print "And the winner is...\n\n   ", max_index, "!!!"
	print "\n    Wooooow!\n"
	print "just checking:", score
	"""
	print 10*"-"
	
	raw_input ("press key to get the winner...")
	
	result(score)
	
	
	
	"""
	if max_index == 0:
		print "The winner is Skoda!"
	elif max_index == 1:
		print "The winner is Nissan!"
	elif max_index == 2:
		print "The winner is Audi!"
	else:
		print "Ooops! Nobody finished?"
	"""
	"""
	for index, value in score:
		if value == winner:
			winnerIndex = index
			if winnerIndex == 0:
				print "The winner is Skoda!"
			elif winnerIndex == 1:
				print "The winner is Nissan!"
			elif winnerIndex == 2:
				print "The winner is Audi!"
			else:
				"Ooops! Nobody finished?"
	"""
		


#Results table for calculation and keeping the score of each player
#also can show final results and the tournament winner
class Results (object):

	pass

#Map for transfer from one race to another
class Map (object):

	pass

gameStart = Race()
game = Engine(gameStart)
game.play()


