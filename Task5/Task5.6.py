
fileHandler = open ("Doc.txt", "r")

listOfLines = fileHandler.readlines()

for line in listOfLines:
    if len(line.strip()) % 2 == 0:
        print(line.strip())

fileHandler.close()
