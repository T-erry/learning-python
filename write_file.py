#To write to a Python file, we need to open it in write mode using the w parameter.

text = "\n Have a nice day! See ya!!" 

with open("copy.txt", "a") as file:
    file.write(text)