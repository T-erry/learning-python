#using with open() will close your file automatically for you after they've been opened
try:
    with open("Python Introduction/test.txt") as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)
    print("wrong path!")


