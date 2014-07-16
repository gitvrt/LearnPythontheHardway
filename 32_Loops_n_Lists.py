names = ['rat','bat','cat','apple','dog','eagle']
print "\nlength of the list is ",len(names)

print "List elements are :"
for name in names:
	print "%s"%name



print "\nSorted list after using sorted(names)\n"
for name in sorted(names):
	print "%s"%name

print "\nReversing after using sorted(names,reverse=False)\n"
for name in sorted(names,reverse=True):
	print "%s"%name
	
newlist = []
print "Now lets prepare another list"
print "Please mention the list size : "
lsize = int(raw_input('>'))

print "\nPlease enter %d elements"%lsize
for i in range(0,lsize):
	newlist.append(int(raw_input()))

print "New List elements are :"
for ele in newlist:
	print "%d"%ele
	
print "\nNew List after sorting are :",sorted(newlist)
for ele in sorted(newlist):
	print "%d"%ele


print "\nNew List after Sorting in reverse Order are :"
for ele in sorted(newlist,reverse=True):
	print "%d"%ele