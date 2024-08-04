""" 
WAP to print the multiplication table of a numbers n using range().
"""
num = int(input("Enter num: "))

for i in range(1,11,1):      # 1 = start point
    print(num * i)           # 11 = stop point
                             # 1 = increment by 
                             # i = store in sequence of values which is increment by one
