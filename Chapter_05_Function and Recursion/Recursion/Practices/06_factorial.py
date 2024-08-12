# WARF to print Factorial of n numbers
'''    
  0! = 1   
  1! = 1    -> By default

  2! = 1 * 2                      or 2 * 1!
  3! = 1 * 2 * 3                  or 3 * 2!  
  4! = 1 * 2 * 3 * 4              or 4 * 3!
  5! = 1 * 2 * 3 * 4 * 5          or 5 * 4!

  so, 
  n! = 1 * 2 * 3 * 4 * 5 * (n-1) * n

  format:
     n! = n * n(n-1) 

'''

def cla_fact(n):
    if(n== 0 or n==1):
        return 1
    else:
        return n * cla_fact(n-1)

num = int(input("Enter your number: "))

fact = cla_fact(num)
print(f"Factorial of {num} : {fact}")
       