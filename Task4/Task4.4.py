Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

def liststodict(func):
    def wrapper():
        func()
    return wrapper

def zipfunction():
    a = zip(Student,capital)
    print('The output dictionary using zip function',dict(a))

def dict_comprehension():
    res = {Student[i]: capital[i] for i in range(len(Student))}
    print('The output dict using Dictionary comprehension:',res)

zipper = liststodict(zipfunction)

comprehension = liststodict(dict_comprehension)

zipper()
comprehension()
