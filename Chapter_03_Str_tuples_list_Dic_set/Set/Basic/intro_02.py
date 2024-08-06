""" 
Topic: set of python
obj: A built-in data type that stores unique values. It is unordered collection of items.

-> we can pass(add) as element
      --> int
      --> double
      --> tuple

-> we can't pass(add) as element
      --> list
      --> dictionary
      --> set
"""
# create set
set_1 = {"Kz", 4039, 40.30, "Raihan"}

# add some new items as immutable data type

set_1.add("Dhaka")  # str type data element
set_1.add(98.89)    # double type data element
set_1.add((91.01, 95.07,88.90)) # tuple type data element

print("Set_1: ",set_1) 

""" 
 We can't pass or add items as mutable data type
 set_1.add(["BD", "Country", "CSE4039"])
 set_1.add({"name": Kz, "Id": 4039, "Marks": 32.23})
"""
