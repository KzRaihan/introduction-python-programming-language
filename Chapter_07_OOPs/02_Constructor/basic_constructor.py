'''  
Topic: constructor
obj  : constructor is a special type of method that used to initialize object.

-> Syntax:
     def __init__(self):
        # initialization code

-> Note:
   1. It's called automatically when an object is created.
   2. It's used to set initial values for object attributes.
   3. It's not required to define return type for constructor.
   4. It can have any number of arguments.


eg:
  Create Student class that takes name and marks of 3 subjects as arguments in constructor.
  then create a method to print the average
'''

class Person:
    # Constructor to initialize object attributes
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # method to calculate the average of the marks
    def cal_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} \nYour marks : {self.marks}")
        print("Your average marks: ", sum/3)

# Create an object of Person class
s1 = Person("KzRaihan", [97, 98, 96])
s1.cal_avg()

# second object
s2 = Person("Raihan", [90, 99, 94])
s2.cal_avg()