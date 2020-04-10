a = int(input("Enter a limit:"))

def showNumbers(a):
    for i in range(0,a):
        mod = i % 2
        if mod>0:
            print( i, "Odd")
        else:
            print(i, "Even")

evenodd(a)
