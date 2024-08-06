""" 
Topic: set.union() method
obj  : combines both set values and returns new set
      -> when perform set.union() method must be two set need
      -> this method return the values in the new set
      -> duplicate value count only one times
syntax: 
    set_name1.union(set_name2)
"""
# set one
set_1 = {10, 20, 30, 40, 50}
print("Set_01: ", set_1)

# set two
set_2 = {30, 40, "Kz", 60, 70}
print("\nSet_02: ", set_2)

# use set.union() method
set_3 = set_1.union(set_2)
print("\nSet_03: ", set_3)

# simple example
set_01 = {1, 2, 3}
set_02 = {3, 4, 5}

print("\nSet_01: ",set_01)
print("Set_02: ",set_02)
# combine both set values and return new set
set_03 = set_01.union(set_02)
print("\nset_03: ", set_03)