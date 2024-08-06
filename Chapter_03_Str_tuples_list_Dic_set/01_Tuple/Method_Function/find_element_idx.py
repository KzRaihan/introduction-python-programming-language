""" 
 Topic: tup.index(element)
 obj  : return index of first occurence

 >> Syntax: 
      top.index(element)
"""
# eg_01 
tup = (10, 20, 30, 40, 50)
print("30 element idx: ", tup.index(30)) # o/p: 2

# eg_02 same element is present multiple times in tuple
mul_num = (10, 20, 30, 40, 20, 50, 30)
print("20 idx for first time: ", mul_num.index(20)) # o/p: 1

print("30 idx for first occurence: ", mul_num.index(30)) # o/p : 2