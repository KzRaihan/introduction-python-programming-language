'''  
Topic: instance vs class attributes

Precedence order: instance attributes > class attributes

-> instance variable:
    --> declared inside the class And inside the method.
    --> each object(instance) has its own copy of instance variable.
    --> memory occupied large(dependance on the how many objects are created).
    --> can be accessed using object reference.(eg. object1.name)
    --> can be modify using object reference.

-> class variable:
    --> declared inside the class And outside the method.
    --> shared by all objects of that class.
    --> memory occupied small(independent).
    --> can be accessed using class name.(eg. Main_book.book_name)
    --> can't be modify using object reference.
    --> can be modify using class name.


'''
class Student:
    # class attribute
    university_name = "SU"

    # instance attributes
    def __init__(self, name, id): # this are the instance attribute
        self.name = name   
        self.id = id
    
    # method
    def display_info(self):
        print("University Name:", Student.university_name)
        print("               :", self.name)
        print("ID             :", self.id)

# Create objects of the student class

# first object : access the instance attributes

first = Student("KzRaihan", 4039)  # first = object name
first.display_info()

# access the class attributes

print("University Name:", Student.university_name) # by using class name  

