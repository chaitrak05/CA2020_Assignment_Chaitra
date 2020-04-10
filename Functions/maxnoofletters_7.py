a = str(input("Enter First string:"))
b = str(input("Enter Second string:"))


def maxlength(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    elif len(a) == len(b):
        print(a,b)

maxlength(a,b)
