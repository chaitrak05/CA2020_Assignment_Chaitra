from sys import argv

script, filename = argv
print(filename)
while True:
    try:
        txt = open(filename)
        print("The filename exists:",filename)
        break
    except IOError as E:
        print('File Not Found')
        print("Enter the file name")
        filename = input("> ")
