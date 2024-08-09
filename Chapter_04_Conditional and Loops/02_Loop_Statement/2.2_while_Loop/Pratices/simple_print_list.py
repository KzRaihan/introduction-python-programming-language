"""   
-> 1. print the elements of the following list using loop
      [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

-> 2. search for a number x in this tuple using loop
      (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
       
"""
# eg_01: print list using while loop
list_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("Given list values are: ")
i = 0
while i < len(list_num):
    print(list_num[i])
    i += 1

# eg_02: search a element from tuple
tup_num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

print("\nExample two : finding the item for given tuple: ")
print(tup_num)

"""  
using while loop to print tuple values
i = 0
while tup_num[i] <= len(tup_num):
    print(tup_num[i])
    i += 1
"""

search_item = int(input("Enter your search item: "))
idx = 0

while idx < len(tup_num):
    if tup_num[idx] == search_item:
        print("Item found at idx: ", idx)
    idx += 1
