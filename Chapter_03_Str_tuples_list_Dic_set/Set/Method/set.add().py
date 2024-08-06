""" 
Topic: set.add(element) method
obj  : adds an element

Syntax:
    set_name.add(element)
"""
# eg_01: first create an empty set then using set.add() method to store some element within empty set

set_empty = set()

set_empty.add(10)
set_empty.add(20)
set_empty.add(30)

print("Set element 01 :", set_empty)  # output: {10, 20, 30}
print("length: ", len(set_empty))       # o/p: length: 3

set_empty.add(30) # duplicate or repeated value elements store only once time
print("\nSet element 02 :", set_empty)  # output: {10, 20, 30}
print("length: ", len(set_empty))   # o/p: length: 3

set_empty.add(50)
set_empty.add("Kz")
set_empty.add("Raihan")
set_empty.add(4039)
set_empty.add(98.023)

print("\nSet element 03 :", set_empty)  # output: {10, 20, 30, 4039, 50, 'Kz', 'Raihan', 98.023}
print("length: ", len(set_empty))   # o/p: length: 8

