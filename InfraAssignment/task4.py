# Given a file name or prefix, the program scans all the drives and folders recursively and retrieves the info of all the files matching with it.
# Written by J. Aravind Babu

import os
import re

name = raw_input("Enter the file name or prefix to be searched: ") # file name or even prefix can be given as input


result = []
for root, dirs, files in os.walk("/home"): # scanning the whole system
	for f in files:
		if re.match(name,f): # searching for a regular expression match with the given input name
			result.append((f,os.path.join(root, f)))

if len(result) == 0:
	print "No files found" # printing only if any files are found
else :
	print "Files with the given name :",name,"\n"
	for match in result:
		print "File name : ",match[0]
		print "Location : ",match[1],"\n"
		print "---------------------------------------------------"
