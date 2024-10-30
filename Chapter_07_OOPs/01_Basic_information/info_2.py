''' 
Topic: class and object
    
how to direct access the class variable 

'''

# Define the class
class Person:
    # Fields (Class attributes)
    # name = ""
    age = None
    qualification = "BSC"
    
    # Method (Instance method)
    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Qualification:", self.qualification)

# Create an object (first object) and call the method
first = Person()
# directly assign the values of instant(object) by using class attributes
first.name = "KzRaihan"
first.age = 23
first.info()  # This will print the information of the object
print("Type:", type(first)) # class is a user define data type
print("Type: ", type(Person))

