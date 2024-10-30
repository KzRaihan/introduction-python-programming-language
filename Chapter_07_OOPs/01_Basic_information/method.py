'''  
topic: method in class

-> class is the collection of attributes and methods

    -> attributes : data or information
          --> two types
             _-> class attribute
             _-> instance attribute


    -> method : inside the class is called method

'''
class Student:
    # class attribute
    university_name = "SU"
     
    # Constructor: initialize the instance attributes
    def __init__(self, name, id): # instance attribute
        self.name = name
        self.id = id

    # method: to display the name
    def display_name(self):
        print("Name : ", self.name)

    # method: to get the id
    def get_id(self):
        return self.id

        
    # method:  to print the all information
    def display_info(self):
        print("University Name:", Student.university_name)
        print("Name:", self.name)
        print("ID:", self.id)

# Create objects of the student class

first = Student("KzRaihan", 11)
first.display_name()     # calling the display_name() 
print("ID  : " , first.get_id()) # calling the get_id()

# create second objects for student class
second = Student("Raihan", 12)
second.display_info()  # calling the display_info()