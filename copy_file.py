# copyfile() = copies contents of a file
#copy()= copyfile() + permission mode + destination can be a directory
# copy2() copy() + copies metadata (file's creation and modificatio times)

import shutil

shutil.copyfile("copy.txt", 'new.txt')# source, dst