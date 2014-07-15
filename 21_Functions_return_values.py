def add(a,b):
	return a+b

def sub(a,b):
	return a-b
	
def pro(a,b):
	return a*b

def div(a,b):
	return a/b

print "Enter a and b values : "
a=float(raw_input('> '))
b=float(raw_input('> '))
sum=add(a,b)
dif=sub(a,b)
mul=pro(a,b)
div=div(a,b)
print "\nSum of %d and %d is %d"%(a,b,sum)
print "\nDifference of %d and %d %d"%(a,b,dif)
print "\nProduct of %d and %d is %d"%(a,b,mul)
print "\nDivision of %d by %d is %f"%(a,b,div)
