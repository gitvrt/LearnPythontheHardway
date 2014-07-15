def appreciate(participations,medals):
	print "\nYou participated in %d events"%participations
	print "And won %d medals"%medals
	print "Thats Great :) Keep it UP!"

appreciate(10,8)

p = int(raw_input("No of participations ? :"))
m = int(raw_input("No of Medals ? :"))

appreciate(p,m)

appreciate(p+5,m+5)

print "\nThus different types of parameter passing techniques achieved"