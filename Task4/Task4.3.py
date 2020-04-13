# Write a program to Python find out the character in a string which is uppercase using list comprehension.

a = str(input("Enter a sentence with upper and lower case:"))

def uppercase(arg):
    def iterate(arg):
        b = [x for x in arg if x.isupper()]
        return b
    return iterate
    
res = uppercase(a)

print(res(a))
