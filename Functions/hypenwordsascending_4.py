a = str(input("Enter some hypen seperated words :"))

def ascending(a):
    list = [n for n in a.split('-')]
    list.sort()
    print('-'.join(list))

ascending(a)
