# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List of values is ',list)
print('Tuple of values is  ',tuple)