# Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

# try:
#
# except SyntaxError:
#     print('error')


try:
    date = eval('datetime(2009, 12a, 31)')
except SyntaxError:
    print("Syntax Error")
