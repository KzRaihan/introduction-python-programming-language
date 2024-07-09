""" 
 Topic: Indexing in list
 obj : accessing and modify element by using index

 >> Syntax
  list_name[index]
"""
# eg_01: Accessing element
print("Example_01: Accessing element")
list = [22, 11, 33,88, 66, 9]

print("First element  : ", list[0]) # 22
print("Second element : ", list[1]) # 11
print("Third element  : ", list[2]) # 33

# eg_02: Modifying element
print("\nExample_02: modify element")
print(list)
list[0] = 100
list[2] = 500
list[5] = 300

print("After modifying : ", list) # [100, 11, 500, 88, 66, 300]

# eg_03: index limitation
# if we can access only within the range of list
# list[6] = 700 # index error (list index out of range)

single = [100]
print(single)
print(type(single))