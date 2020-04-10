a = input("Enter an alphanumber character:")\

freq =  []
b = list(filter(lambda x: x.isalpha(),a))

for i in b:
    freq.append(b.count(i))

for i,word in enumerate(b):
    print(word,'=',freq[i])
