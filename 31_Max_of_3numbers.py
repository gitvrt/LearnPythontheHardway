print "Please enter 3 Numbers"
a = int(raw_input('> '))
b = int(raw_input('> '))
c = int(raw_input('> '))

if a>=b and a>=c:
	print "%d is greater than %d and %d "%(a,b,c)
elif b>=c:
	print "%d is greater than %d and %d "%(b,a,c)
else:
	print "%d is greater than %d and %d "%(c,a,b)