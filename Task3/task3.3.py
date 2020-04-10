
#Write a program to get the sum and multiply of all the items in a given list.
list1 = [1, 2, 3,4]
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

def addlist(myList):
    result = 0
    for x in myList:
        result = result + x
    return result

print(multiplyList(list1))
print(addlist(list1))
