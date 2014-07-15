def print_two(arg1,arg2):
	print "Hai I am Print_two Function"
	print "I can print two Strings/Numbers"
	print "arg1 : %r and arg2 : %r"%(arg1,arg2)
def print_none():
	print "Hai I am Print_none Function"
	print "Nothing to print here"

one = raw_input("Enter a String/number : ")
two = raw_input("Enter another String/number : ")
print_two(one,two)
print_none()