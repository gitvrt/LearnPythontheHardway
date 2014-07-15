from sys import argv
scriptname,filename = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) #to the starting of file
	#f.seek(2) to the end of file
	#f.seek(1) from the current position exactly
	#f.seek(-3,2) to the 3rd byte from the end
def print_line(f):
	print f.readline()

current_file = open(filename)

print "\nPrinting entire File"
print_all(current_file)

print "\nRewinding"
rewind(current_file)

print "\nPrinting line by line\n"

print_line(current_file)
print_line(current_file)
print_line(current_file)

current_file.close()