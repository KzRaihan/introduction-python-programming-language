"""  
-> 1. WAP to Keep taking numbers as input from user, until user enters an odd numbers
-> 2. WAP to Keep taking numbers as input from user, until a numbers which is multiple of 7
"""
# eg_01:
print("\nExample one: When entered any odd numbers then terminate")
while 1:
    num = int(input("Enter any integer: "))
    if(num%2 != 0):
        print("Your entered an odd number")
        break

# eg_02:
print("\nExample Two: When entered number which is multiple by 7 then terminate ")
 
while 1:    # always true
    num = int(input("Enter any integer: "))
    if(num % 7 == 0):
        print("Your entered ", num , " which is multiple by 7")
        break