"""  
Topic: Set in python
obj : set are the unordered collection of union elements.
     - It is mutable(changeable)
     - set doesn't allow duplicate values.

syntax: set_name = {value1, value2,....}
     -> set_name is similar to variable name
     -> each value in the set must be unique and immutable(not changeable)
     -> set value can be 
                     --> boolean
                     --> integer    # which are immutable
                     --> float
                     --> string
                     --> tuple
    -> set value can't be 
                    --> list
                    --> dictionary    # which are mutable 
                    --> set
"""
# Declare or create a set 
set_01 = {10, 20, 30, 40, 50}

# Access the elements of the set
print("Set Element: ", set_01)
print("Type: ", type(set_01)) 

# Repeated or duplicate elements stored only once 
set_02 = {"Kz","Raihan", 4039, "CSE", 50.50}
print("\nSet Element: ", set_02)  # o/p: {'Kz', 'Raihan', 4039, 'CSE', 50.50}
print("length: ", len(set_02))    # o/p: 5