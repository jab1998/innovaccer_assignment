#The program should scan all the Drives and folders like C:/User/* (Windows) and /home/* (Linux) recursively and then identify the top 10 files which have the largest size on the system.
# Written by J. Aravind Babu

import os
import math

pairs=[]
for (dir, _, files) in os.walk("/home"): #Here the path can be changed to 'C:/User/*' for running the program in Windows
	for f in files:
		path = os.path.join(dir, f)
		if os.path.exists(path):
			pairs.append((f,math.ceil((os.path.getsize(path)/1000000.0)*100)/100,os.path.realpath(path))) #converting bytes to MB and rounding off to two decimal places 
       

#Sorting the files in descending order and extracting the top ten

sorted_list = sorted(pairs,key=lambda s: s[1],reverse=True)[:10] # this 10 can be changed to extract that many number of files 

print "The top ten largest files: ","\n"
#Printing the top ten files extracted along with their sizes in MB and also location
for triplet in sorted_list:
	print "File name : ",triplet[0]
	print "Size : ",triplet[1],"MB"
	print "Location : ",triplet[2] ,"\n"
	print "----------------------------------------------------"
