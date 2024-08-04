"""
use only : while loop  
    -> 1. print numbers form 1 to 100
    -> 2. print numbers form 100 to 1
    -> 3. print the multiplication table of a number of n

"""
print("\nExample 1: print 1 to 100\n")
# start: 1 
# end  : 100
# inc  : 1
i = 1
while(i<=100):
    print(i)
    i += 1

print("\nExample 2: print 100 to 1\n")
# start: 100 
# end  : 1
# drc  : 1
i = 100
while(i >= 1):
    print(i)
    i -= 1

print("\nExample 03: multiplication table of given input\n")

num = int(input("Enter number to which table do you want: "))
i = 1
while i <= 10:
    print(num ,"X", i ," : " ,num * i)
    i += 1

