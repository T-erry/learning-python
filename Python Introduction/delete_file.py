import os
import shutil

try:
    path ="Python Introduction/deletion.txt"
   # os.remove(path) #delete an empty file
    #os.rmdir(path) # delete an empty directory
    #shutil.rmtree(path)# delete a directory containing files
except FileNotFoundError:
    print("Path not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path)