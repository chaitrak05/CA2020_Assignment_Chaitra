
#1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

C= 50
H = 30
Ds = []
result =[]
Dv=input("Enter the value for D in comma sepated sequence:")
Ds=Dv.split(",")
Ds = [int(i) for i in Ds]
i=0
l = len(Ds)
while(i<l):
    Q = round(math.sqrt((2*C*Ds[i])/H))
    result. append(Q)
    i+=1
print("output=",result)