from sys import argv

scriptname,fname = argv

txt = open(fname)

print "%s Contents : "%fname,txt.read()