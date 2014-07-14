from sys import argv

scriptname,fname = argv

print "Do you want to erase the %s file contents " %fname
print "Press Ctrl-C to quit or Enter to Continue "

raw_input("?")

target = open(fname, 'w')

print "Truncating %s file Contents " %fname
target.truncate()

print "Please enter 3 lines to write to file"

line1 = raw_input("Line-1 :")
line2 = raw_input("Line-2 :")
line3 = raw_input("Line-3 :")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And Finally we Close %s"%fname
target.close()