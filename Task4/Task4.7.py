Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

def liststodict(func):
    def wrapper():
        func()
    return wrapper

def zfunc():
    a = zip(Student,capital)
    print('The output dictionary using zip function',dict(a))


combine = liststodict(zfunc)

combine()
