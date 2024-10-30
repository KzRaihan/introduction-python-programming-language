'''   
topic: self parameter
   
obj  : -> Calling methods from within the same class. 

'''
class Person:
    # Constructor (__init__) method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_mobile(self, name, age, mobile):
        self.__init__(name,age)
        self.mobile = mobile
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

# Create an object (first object) and call the method
first = Person("KzRaihan", 23)
first.display_info()

first.set_mobile("Raihan", 22, 770)
first.display_info()

'''
Here, the set_mobile method is calling the __init__ method by using the self parameter. This is known as self parameter. When we call a method from within the same class, Python automatically passes the instance as the first argument to the method.
'''