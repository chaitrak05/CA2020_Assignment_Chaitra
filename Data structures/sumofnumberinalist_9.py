x=[1,2,3,4,5,6,7,8,9,-1]

lookup = {}
for i, num in enumerate(x):
    if 8 - num in lookup:
        print (lookup[8 - num],'+', num ,'= 8')
    lookup[num] = num
