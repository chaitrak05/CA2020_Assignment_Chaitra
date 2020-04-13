def div_num(x):
    def divisible_check(y):
        li = []
        for i in range(x, y):
            if (i%7==0) and (i%3!=0):
                li.append(str(i))
        return li
    return divisible_check


div = div_num(0)

result =  div(5000)

print(result)
