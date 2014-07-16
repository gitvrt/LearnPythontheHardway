print "Program on While Loop"
i = 0
list = []

print "\nPlease mention list size"
size = int(raw_input('> '))

print "\nPlease Enter %d number of elements\n"%size
while i < size:
	list.append(int(raw_input('> ')))
	i += 1 

print "\nList elements are :\n"
j = 0
while j<len(list):
	print "%d\t"%list[j]
	j += 1


