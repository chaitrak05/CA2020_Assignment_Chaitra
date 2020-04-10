
even_list = []
odd_list = []

while True:
    e = int(input("Enter a number between 1 to 50:"))
    if e%2==0:
        even_list.append(e)
    else:
        odd_list.append(e)
    if len(even_list) == 5:
        print("The sum of even numbers entered :", sum(even_list))
        print("The maximum of even numbers entered:", max(even_list))
        break
    elif len(odd_list) == 5:
        Total = sum(odd_list)
        print("The sum of odd numbers entered :", sum(odd_list))
        print("The maximum of odd numbers entered:", max(odd_list))
        break
