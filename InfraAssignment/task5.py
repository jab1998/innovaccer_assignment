# Given the path of directory, the program compresses the directory and creates the zip file
# Written by J. Aravind Babu

import os
import shutil

dir_name = raw_input("Enter the full path of the folder to be compressed: ") # taking the path of the folder(or) directory to be compressed
output_filename = dir_name

print "\n"
# creating the archive of the given directory
if os.path.exists(dir_name):
	shutil.make_archive(output_filename, 'zip', dir_name)
	print "Archive created successfully \n"
else:
	print "No such path or directory exists\n"


