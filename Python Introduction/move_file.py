import os

source = "Python Introduction/move.txt"
destination = "//home//terry-tech//fun-projects//move.txt"


try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source, destination)
        print(source+ "was moved")


except FileNotFoundError:
    print(source + "was not found")

