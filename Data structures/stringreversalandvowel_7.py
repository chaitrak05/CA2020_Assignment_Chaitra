a = str(input("Enter a string:"))

def string_reversal(a):
    stringlength=len(a)
    slicedString=a[stringlength::-1]
    vowels = ['a','e','i','o','u']
    for num, letter  in enumerate(slicedString,start = 1) :
        if letter in vowels:
            print(letter , num)
    print('Reversed String :',slicedString)


string_reversal(a)
