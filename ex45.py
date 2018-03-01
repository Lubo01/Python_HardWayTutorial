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
#start with Design

#Game Engine to play 
class Engine (object):

	def __init__(self,race):
		pass
	def play (self):
		pass
	

#Race class for 5 Races with description and dice rolling
class Race (object):

	print "Get ready, game is starting..."
	pass

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


