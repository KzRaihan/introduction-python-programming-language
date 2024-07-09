""" 
  Topic: Tuple slicing
  objective: Accessing a part of tuple

  -> Syntax:
      tuple_name[start_index:end_index] # end_index is not include
"""
# eg_01
tup =("Raihan", 23,"Learn python", 2024)
tup1 = tup[1:3] # 1-2 indx element are access which are 23, Learn python
print(tup1)  # print

# eg_02 first index is not assign
num = (10,20,30,40,50)
print(num[:4]) # first index = 0 is automatic assign(0-3) idx element are access

# eg_03 last(end) index is not assign
print(num[2:]) # 2-last element(length of num ) are assign

# eg_04 using  negative idx to access tuple element
# NNB : By using negative idx access by tuple elements then first idx always is smaller than last idx

num1 = (100.11, 222.22, 333.33, 400, 500)
#    num1[-5] = 100.11
#    num1[-4] = 222.22  in this way to store in memory
#    num1[-3] = 333.33 
#    num1[-2] = 400 
#    num1[-1] = 500

print("access element(-5 to -2) : ", num1[-5:-1]) # -5 to -2 idx element are access
# print("access all element:", num1[-1:-5]) # empty element are access
print("Access all element : ", num1[-5:len(num1)])
print("Access(-4 to -3): ", num1[-4:-2]) # end idx is not include

# accessing element by positive idx
print("Access all element : ", num1[:len(num1)])
print("Access all element : ", num1[0:len(num1)])


