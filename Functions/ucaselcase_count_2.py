a = str(input("Enter a string:"))

ucount = 0
lcount = 0

def ulcaseCount(a,ucount,lcount):
    for i in a:
        if (i.islower()):
            lcount += 1
        elif(i.isupper()):
            ucount += 1
    return ucount, lcount
    print("No. of Upper case characters : ", ucount)
    print("No. of Lower case characters : ", lcount)

ucount,lcount = ulcaseCount(a,ucount,lcount)

print("No. of Upper case characters : ", ucount)
print("No. of Lower case characters : ", lcount)
