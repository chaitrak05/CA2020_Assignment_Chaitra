list = []

def uppercase(l,list):
        list.append(l.upper())
        return list

while True:
    l = input()
    if l:
        list = uppercase(l,list)
    else:
        break

for l in list:
    print(l)
