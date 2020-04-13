# Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits”


a = str(input('Enter a four digit number:'))

if len(a)>4:
    raise Exception('Enter only 4 digits')
