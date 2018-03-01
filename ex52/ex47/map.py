#52 Web game map

class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)
		
central_corridor = Room ("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship...

You're running down the central corridor to the Weapons Armory...
He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room ("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke...
You do a dive roll into the Weapon Armory...
...neutron bomb in its container. There's a keypad lock on the box
and you need the code to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits.
""")

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks...
You burst onto the Bridge...
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb...
Now that the bomb is placed you run to the escape pod to
get off this tin can.

There's 5 pods, which one
do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space...
You won!
""")
the_end_loser = Room("The End",
"""
You jump into a random pod...
The pod escapes... then implodes...
""")

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

generic_death = Room("death", "You died.")

death_cen_corr_shoot = Room("death", 
"""
Quick on the draw you yank out...
makes him fly into an insane rage...
Then he eats you.
""")

death_cen_corr_dodge = Room("death", 
"""
Like a world class boxer you dodge...
Gothon stomps on your head and eats you.
""")

death_las_weap_arm = Room("death", 
"""
The lock buzzes one last time...
Gothons blow up the ship from their ship and you die.
""")

death_bridge_throw = Room("death", 
"""
In a panic you throw the bomb...
Gothon shoots you right in the back killing you.
""")

the_bridge.add_paths({
	'throw the bomb': death_bridge_throw,
	'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
	'0132': the_bridge,
	'*': death_las_weap_arm
})

central_corridor.add_paths({
	'shoot!': death_cen_corr_shoot,
	'dodge!': death_cen_corr_dodge,
	'tell a joke': laser_weapon_armory
})

START = central_corridor

