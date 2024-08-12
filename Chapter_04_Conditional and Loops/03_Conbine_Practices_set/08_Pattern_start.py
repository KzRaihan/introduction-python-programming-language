""" 
WAP to print the following start pattern
        
         *
        ***       -> for n= 3
       *****  
"""
num = int(input("Enter number: "))

for i in range(1, num+1):
    print(" " * (num-i), end =" ")  # for space
    print("*" * (2*i-1))    # for print *
   
