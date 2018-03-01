#exercise 43 
#try to code a game from basic construct:

"""
Game  description:
"Aliens have invaded a space ship and our hero has to go through a maze of rooms
 defeating them so he can escape into an escape pod to the planet below. The game
 will be more like a Zork or Adventure type game with text outputs and funny ways
 to die. The game will involve an engine that runs a map full of rooms or scenes.
 Each room will print its own description when the player enters it and then tell
 the engine what room to run next out of the map."

At this point I have a good idea for the game and how it would run, so now I want to describe each scene:

Death
    This is when the player dies and should be something funny.
Central Corridor
    This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing.
Laser Weapon Armory
    This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
The Bridge
    Another battle scene with a Gothon where the hero places the bomb.
Escape Pod
    Where the hero escapes but only after guessing the right escape pod. 
"""

global var_next_scene
var_next_scene = 'start'

class Scene(object):
	
	def enter(self):
		print "Now, think carefully and choose wisely..."
		input = raw_input("> ")
				
class Engine(object):
	
	def __init__(self, scene_map):
		pass
	def play(self):
		pass

class Death(Scene):
	
	def enter(self):
		print "1. You pretend to be a monster too, but looks awkward."
		print "2. You try to ignore monsters and just walk away."
		print "3. You yell on them and start giving orders to monsters as their commander."
		
		input = raw_input("> ")
		
		print "Monsters caught you quickly, put you on fire and eat you.\n"
		print "This is the end. You have lost.\n"
		
		global var_next_scene
		var_next_scene = 'EndOfGame'

death = Death()		
		
class CentralCorridor(Scene):
	
	def enter(self):
		print "Now, think carefully and choose wisely..."
		print "1. Fight Gothon monster with your bare hands."
		print "2. Try to make monster laugh with a joke."
		
		input = raw_input("> ")
		
		if input == "1":
			print "Gothon smacks you with one hand and you don`t know what was next.\n"
			
			global var_next_scene
			var_next_scene = 'Death'
					
		elif input == "2":
			print "Yee, good joke. Monster laughed and you escaped through the nearest door.\n"
			
			global var_next_scene
			var_next_scene = 'LaserWeaponArmory'
		
		else:
			print "Oops! The code is scary and messed up!" #ValueError message
			
corridor = CentralCorridor()

class LaserWeaponArmory(Scene):

	def enter(self):
		print "Now, think carefully and choose wisely..."
		print "1. Will you take a neutron bomb on left side of the Armory?"
		print "2. Or you`ll rather choose a python snake in the corner?"
		
		input = raw_input("> ")
		
		if input == "1":
			print "You feel that the bomb is really heavy...\n"
			
			global var_next_scene
			var_next_scene = 'TheBridge'
					
		elif input == "2":
			print "Python friend hugs you strongly...\n"
			
			global var_next_scene
			var_next_scene = 'Death'
		
		else:
			print "Oops! The code is scary and messed up!" #ValueError message

laser = LaserWeaponArmory()
			
class TheBridge(Scene):

	def enter(self):
		print "You put neutron bomb in front of bridge and crossed the bridge to the dark side.\n"
		print "As you look over shoulder, you see monsters at the bridge"
		print "destroyed away after bomb explosion.\n"
		
		global var_next_scene		
		var_next_scene = 'EscapePod'

bridge = TheBridge()
		
class EscapePod(Scene):

	def enter(self):
		print "Now, think carefully and choose wisely..."
		print "1. Left pod"
		print "2. Central pod"
		print "3. Right pod"
		
		input = raw_input("> ")

		if input == "1":
			
			print "You feel cold as you entered...\n"
			
			global var_next_scene
			var_next_scene = 'Death'
					
		elif input == "2":
			
			print "You feel cold as you entered...\n"
			
			global var_next_scene
			var_next_scene = 'Death'
		
		elif input == "3":		
			
			print "Yes! The ship is yours and you escaped!\n"
			print "This is the end. You have won."
			
			global var_next_scene
			var_next_scene = 'EndOfGame'
		
		else:
			print "Oops! The code is scary and messed up!" #ValueError message
			
escape = EscapePod()
		
class Map(object):

	def __init__(self, start_scene):
	
		# ? self.start_scene = start_scene
		
		if start_scene == 'central_corridor':
			print "Hello new hero! Welcome at Gothon planet!"
			print "You are standing in Central Corridor with Monster in front of you."
			print "You see 3 doors and a window. You`d better prepare to fight!\n"
			
			corridor.enter()
						
		else:
			print "Oops! The code is scary and messed up!" #ValueError message
					
	def next_scene(self, scene_name):
		
		# ? self.scene_name = scene_name
		
		if scene_name == 'Death':
			print "Finally you reached enlightened place with crowd of monsters at dinner."
			print "You can not escape them, how will you survive?\n"
			
			death.enter()
			
		elif scene_name == 'LaserWeaponArmory':
			print "Wow! You have find the Laser Weapon Armory full of excellent guns!"
			print "Choose the right weapon to fight these invaders!\n"
			
			laser.enter()
			
		elif scene_name == 'TheBridge':
			print "You came to the narrow stone bridge over the volcano lake."
			print "The only way is to the dark other side.\n"
			
			bridge.enter()
			
		elif scene_name == 'EscapePod':
			print "You have fallen down and suffer a pain in your head."
			print "When you look around it seems that there is something black on the right."
			print "You came closer and see that there is a spaceship with three pods.\n"
			
			escape.enter()
			
		else:
			print "Oops! The code is scary and messed up!" #ValueError message
			print "The Game will be closed."
			
			global var_next_scene			
			var_next_scene = 'EndOfGame'
	
	def opening_scene(self):
		
		while var_next_scene != 'EndOfGame':
			
			global var_next_scene
			print var_next_scene
			
			map_instance.next_scene(var_next_scene)


map_instance = Map('start_scene')
			
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

map_instance.opening_scene()



