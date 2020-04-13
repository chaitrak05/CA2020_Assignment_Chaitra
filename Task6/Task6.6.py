# Write a Person class with an instance variable, , and a constructor that takes an integer, ,
 # as a parameter. The constructor must assign  to  after confirming the argument passed as  is not
 #  negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid,
 #  setting age to 0.. In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld() should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
#
# Otherwise, print You are old..

class Person():
    def __init__(self, age):
        if age>0:
            self.age = age
            print(age)
        else:
            raise Exception("Age is not valid")

    def yearPasses(self):
        self.age +=1
        print(self.age)

    def amIOld(self):
        if self.age <= 12:
            print("You are young")
        elif self.age in range(13,18):
            print("You are a Teenager")
        elif self.age >= 60:
            print("You are old")



b = Person(59)
b.yearPasses()
b.amIOld()
