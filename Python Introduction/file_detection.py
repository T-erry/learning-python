import os
path = "/home/terry-tech/fun-projects/monaco"

if os.path.exists(path):
    print("That location exist!")

    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesn't exist!")