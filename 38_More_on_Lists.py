numbers = "Zero One Two Three Four Five"

print "Now we will split the above string using split()"

stuff = numbers.split(' ')
more_stuff = ["Day" , "Night" , "Song" , "Frisbee" , "Corn" , "Banana" , "Girl" , "Boy"]

print "After splitting numbers : ",stuff," \nLength of the splitted list is",len(stuff)

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "\n I am adding :",next_one
	stuff.append(next_one)
	print "There are %d items in the stuff now"%len(stuff)
	
print "And finally stuff is ",stuff

print "\n some more operations on stuff"

print "stuff[1] is ",stuff[1]
print "stuff[-1] is ",stuff[-1]
print "stuff[-3] is ",stuff[-3]
print "stuff.pop() is ",stuff.pop()
print "'  ___  '.join(stuff) is ",'  __  '.join(stuff)
print "'#'.join(stuff[3:7]) is ",'#'.join(stuff[3:7])
print "Final stuff ",stuff