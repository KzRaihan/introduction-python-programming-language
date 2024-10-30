'''   
Topic: Self Parameters
obj : reference to the current instance of class

  -> refers to the current instance(object) being create
     It allows to access the instance attributes and method.
  
  
  -> To differentiate(eliminate) between instance variables and local variables.
     need to assign values to the object's attribute.


  -> Calling methods from within the same class.  

'''
# By using self parameter to initialize the instance attribute
class Person:
    # Constructor (__init__) method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method (Instance method)
    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create instance's of Person class

# first object(instance)
first = Person("Kz", 23)
first.info()

# second object
second = Person("Raihan", 22)
second.info()