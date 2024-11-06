# file = 'nofilehere.txt'
# readfile = open(file, 'r')
# print(readfile.read())
try:
    filename = 'nofilehere'
    readfile = open(filename, 'r')
except IsADirectoryError:
    print(f"Sorry, {filename} is a directory")
except FileExistsError:
    print(f"Sorry, {filename} does not exist")
except FileNotFoundError:
    print(f"Sorry {filename} was not found")
else:
    print("Everything is cool")
    readfile.close()
finally:
    print(f"Thanks for stopping by my friend !")