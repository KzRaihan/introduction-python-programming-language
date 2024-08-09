"""  
-> 1. WAP to print the element of the following list using for loop
   
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100

-> 2. search for a number x in this tuple
      
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100
           
"""
print("Solution Prb one: ")
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for el in nums:
    print(el)

print("\nExample two: finding item from given tuple")


tup_num =(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

search_val = int(input("Enter your Search item: "))

idx = 0
for el in tup_num:
    if(el == search_val):
        print("Search item is found at idx: ", idx)
    idx += 1

