'''
Topic: OOP concept in Python


> OOP has four core concepts
    -> Encapsulation
    -> inheritance 
    -> Polymorphism
    -> abstraction

> Apart from this concepts
    -> class, objects
    -> constructor
    -> destructor
    -> method overloading, overriding
    -> static method
    -> Different type of keywords(static, final, super)
       etc 



'''
# How to create an class and objects

# Define the class
class Person:
    # Fields (Class attributes)
    name = "KzRaihan"
    age = 23
    qualification = "BSC"
    
    # Method (Instance method)
    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Qualification:", self.qualification)

# Create an object (first object) and call the method
first = Person()
first.info()  # This will print the information of the object

'''
 here, 
   class = Person
   object = first
'''
