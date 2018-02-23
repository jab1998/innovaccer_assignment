# Given a specific file size in MB, the tool lists out all the files in the system which are greater than the given input file size.
# Written by J. Aravind Babu


import os
import math


pairs=[]

data = input("Enter the size in MB: ") # The size is taken as an integer input here

for (dir, _, files) in os.walk("/home"): # scanning all the files in the system
	for f in files:
		path = os.path.join(dir, f)
		if os.path.exists(path):
			pairs.append((f,math.ceil((os.path.getsize(path)/1000000.0)*100)/100,os.path.realpath(path)))
			#converting bytes to MB and rounding off to two decimal places 

       

pamba = sorted(pairs,key=lambda s: s[1],reverse=True)

print "Files which are greater than",data,"MB :\n"
for triplet in pamba:
	if triplet[1] > data: # printing the details of the files which are larger than the given input size
		print "File name : ",triplet[0]
		print "Size : ",triplet[1],"MB"
		print "Location : ",triplet[2],"\n"
		print "---------------------------------------------------"
