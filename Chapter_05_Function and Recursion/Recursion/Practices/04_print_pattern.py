'''    
 WARF to print first n lines of the following pattern
       
        ***
        **         for n = 3
        *
'''
def pattern(num):            # Recursive function
    if(num == 0):            # base case
        return
    else:
        print("*" * num)     # works
        pattern(num - 1)


num = int(input("Enter the number of lines: "))

pattern(num)  # calling the recursive function
