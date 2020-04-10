import operator
from functools import reduce


lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
joinedlist = reduce(operator.add, lists)

print(joinedlist)
