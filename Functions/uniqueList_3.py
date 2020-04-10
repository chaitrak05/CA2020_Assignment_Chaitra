list = [10,20,30,40,10,20,40,50]


def uniqueList(list):
    list1 = []
    for i in list:
        if i not in list1:
            list1.append(i)
    print(list1)

uniqueList(list)
