a = str(input("Enter a string:"))

def string_reversal(a):
  stringlength=len(a) # calculate length of the list
  slicedString=a[stringlength::-1] # slicing
  print (slicedString) # print the reversed string


string_reversal(a)
