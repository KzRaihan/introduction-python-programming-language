""" 
 Topic: list slicing
 obj : Access the part of list or sublist
 
 -> Syntax:
   list_name[starting idx : ending idx]  # ending idx is not include
   NNB: Always starting idx is smaller than ending idx
"""
# eg_01: 
        # 0          1              2       3      4         5     <- idx
lst = ["Raihan", "Kamruzzaman", "Islam", "Ali", "shovo", "Rahim"]

# Accessing sublist from 1 to 3
print(lst[1:4]) # 4 idx is not include to display

# Accessing sublist from 0 to 3 where 0 idx is automatic assign
print(lst[:4]) # 4 idx is not include to display

# Accessing sublist from 3 to end where end idx is automatic assign
print(lst[3:]) # 3 idx is not include to display

# another way to print by using len()
print(lst[3:len(lst)])

# Slicing for negative idx
#       0   1   2   3   4   <- positive idx
num = [10, 20, 30, 40, 50]
#      -5  -4  -3  -2  -1   <- negative idx

print(num[-5:-2]) # 10, 20, 30    (start_idx < end_idx)
print(num[-3: ])  # 30 , 40, 50   end idx is not include

print(num[-5:len(num)]) # 10, 20, 30, 30, 50

