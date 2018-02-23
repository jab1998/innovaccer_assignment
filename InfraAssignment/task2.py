# The tool should sort the files on Desktop on the basis of file extension and move them in separate folders in Documents folder.
# Written by J. Aravind Babu

import os
import sys
from fnmatch import fnmatch
import shutil

source='/home/aravind/Desktop' # The source path from where the files to be sorted can be changed here 

sourcefiles = os.listdir(sourcepath)

destination = '/home/aravind/Documents' # The destination path to where the files are to be moved can be changed here 


fileext="*.*" 

for file in sourcefiles:
	if fnmatch(file,fileext): # matching only the files with extensions to exclude the directories
		ext = os.path.splitext(file)[1][1:] 
		path = destinationpath+'/'+ext
		if not os.path.exists(path): # create a directory only if the directory does not exist
			os.mkdir(path) 
		shutil.move(os.path.join(sourcepath,file), os.path.join(path,file)) #moving the files from source to the concerned folders in the destination

print "Successfully sorted and moved"
    




