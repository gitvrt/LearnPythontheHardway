from sys import argv
from os.path import exists

scriptname,source,destination = argv

print "Copying from %s to %s "%(source,destination)
if exists(destination):
    in_data=open(source,'r').read()
    out_file=open(destination,'w')
    out_file.write(in_data)
    out_file.close()
    print "Copying Done "
else :
    print "Destination file Does not Exist"
	
