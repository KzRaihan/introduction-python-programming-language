"""  
-> 1. WAP to print the sum of first n natural numbers
-> 2. WAP the table of a numbers i/p by user
"""
print("\nExample one: sum of numbers")

num = int(input("enter natural number: "))

i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
    
print("\nSum of ", num ," natural numbers: ", sum)

# example two
print("\nExample two: table of given i/p number:")

tab_num = int(input("enter the numbers: "))

j = 1
while j <= 10:
    print(tab_num ," X ", j, " :", tab_num * j)
    j += 1
