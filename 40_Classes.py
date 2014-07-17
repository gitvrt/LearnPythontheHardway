class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "Thousand years between"
		
	def apple(self):
		print "I am Classy Apples"
		
thing = MyStuff()
thing.apple()
print thing.tangerine


class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy Birthday to you",
					"I dont want to get sued"
					"So I'll stop right there"])

bulls_on_parade = Song(["They really around the family",
						"With Pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()