from sys import exit

def gold_room():
	print "This room is full of gold!! How much do you take (0/1)?"
	next = raw_input('> ')
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number")
	if how_much < 50:
		print "Nice, you are not greedy, you win "
	else:
		print "You are greedy! you loose :("
	
def dead(why):
	print why,'Good try'
	exit(0)
	
def bear_room():
	print "There is a bear Here"
	print "The bear has a bunch of Honey"
	print "The fat bear is in front of another door"
	print "How are you going to move the bear ? "
	bear_moved = False
	
	while True:
		next = raw_input('> ')
		
		if next == 'Take honey':
			dead("The bear looks at you and Kicked off you :(")
		elif next == 'taunt bear' and not bear_moved:
			print "The Bear was moved from the door. you can go through it now"
			bear_moved = True
		elif next == 'taunt bear' and bear_moved:
			print "The bear chewed you leg off"
		elif next == 'open door' and bear_moved:
			gold_room()
def start():
	print "You are in dark room"
	print "There is a door to your right and left"
	print "which onedo you take ?"
	
	next = raw_input()
	if next == 'left':
		bear_room()
	elif next == 'right':
		kaanchan_room()
	else:
		dead('you stumble around the room until you starve')

def kaanchan_room():
	print "You entered starving ghost room whose name is KAANCHANA"
	print "Do you flee for your life or want to become meal for Kaanchana"
	
	next = raw_input()
	if "flee" in next:
		gold_room()
	elif "meal" in next:
		dead("Well! that was tasty")
	else:
		kaanchan_room()
		
start()