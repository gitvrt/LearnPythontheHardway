print "-"*5,"\nUsing Dictionaries {'key' : 'value'} n","-"*5

std_code = {'hyd':'040' , 'blr':'080' , "chn":"044"}

print "\n STD-CODE of HYDERABAD is ",std_code['hyd']

print "\n STD-CODE of BANGLORE is ",std_code['blr']

print "\n STD-CODE of CHENNAI is ",std_code['chn']

std_code['kkr'] = "033"

print "\n",std_code

print "\nDeleting kkr from dictionary"

del std_code['kkr'] 

print "\n Printing of dictionary using for loop : \n"

for city,code in std_code.items():
	print "%s City STD CODE is %s "%(city,code)
	


