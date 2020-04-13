userEmail = 'Chaitrak05@gmail.com'
password = 'Consultadd123'

email = str(input('Enter the email ID:'))
pwd = str(input('Enter the password:'))
for num, i in enumerate(range(2)):
    if pwd == password:
        print("Logged in")
        break
    else:
        pwd = str(input('Retype the password:'))
    if num == 1:
        print("3 attempts Failed!, Please try again later")
