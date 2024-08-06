""" 
 Topics: Tuple indexing
 Objective: Access the elements of a tuple using index.

   - tuple is similar to string
   - tuple is immutable(value is not changeable or modify)
   - 
"""

# eg_01 : Index help to accessing single element
tup = (10,20,30,40,50)

print("First element : ", tup[0]) # 10
print("Second element: ", tup[1]) # 20
print("Third element : ", tup[2]) # 30
print("Four element  : ", tup[3]) # 40
print("Five element  : ", tup[4]) # 50

print("\nType : ", type(tup))

# eg_02: Indexing with out of range number
# print("Six element  : ", tup[5]) # IndexError: tuple index out of range

# eg_03: Empty element print in tuple

empty_tup = ()

print("\nempty tuple : ", empty_tup) # 
print("Type : ", type(empty_tup))

# eg_04: Accessing single value in tuple
tup_01 = ("Kz")  # this is not valid syntax it is count as integer value 
# tup_01 = ("Kz, ") same invalid syntax
tup_02 = ("Kz", ) # this is the valid syntax to assign single value and it's count tuple

print(tup_01) 
print("Type: ", type(tup_01)) # string

print(tup_02) 
print("Type: ", type(tup_02)) # tuple

# eg_05: Negative indexing

print("\nNegative indexing  : ", tup[-1]) # 50
print("Second last element  : ", tup[-2]) # 40
print("Third last element   : ", tup[-3]) # 30
print("Fourth last element  : ", tup[-4]) # 20
print("Fifth last element   : ", tup[-5]) # 10

#eg_06: not changeable or modify(immutable)

tupl = (10, 20, 30, 40, 50, 60)

# tupl[0] = 100 # TypeError: 'tuple' object does not support item assignment
# >> using idx can't change or modify the element
# >> we can not assign 
