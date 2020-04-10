
#Create a new list which contains the specified numbers after removing the even numbers from a predefined list
list=[12,67,23,46,98,30,109,278,300,291,345]
Newlist=[x for x in list if x%2!=0]
print(Newlist)