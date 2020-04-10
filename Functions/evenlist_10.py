
def findeven(a):
    # for i in range(0,21):
    mod = a % 2
    if mod==0:
        return a


filtered = filter(findeven, range(0,21))
print(filtered)

print('The filtered even numbers are:')
for s in filtered:
    print(s)
