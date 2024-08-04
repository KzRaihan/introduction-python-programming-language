"""  
        *** using continue statements ***
        
-> 1. print all odd numbers from 5 to 50.
-> 2. print all even numbers from 1 to 100.
"""
# eg_01
print("\nExample one : odd numbers\n")
i = 5
while i <= 50:
    if(i %2 == 0):  # this is even number cds(all even numbers are skip )
        i += 1
        continue
    print(i)
    i += 1

# eg_02
print("\nExample two : even numbers\n")
i = 5
while i <= 50:
    if(i %2 != 0):  # this is odd number cds(all odd numbers are skip)
        i += 1
        continue
    print(i)
    i += 1

