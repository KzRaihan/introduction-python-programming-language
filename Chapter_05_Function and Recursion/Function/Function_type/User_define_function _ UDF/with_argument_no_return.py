"""  
Topic: UDF function catagories
obj  : with argument no return

with argument:
     -> called function parameters received the values from calling function
        eg: def func(par1, par2)
no return:
     -> calling function doesn't received any data from the called function
       
"""
def fact_cal(num): # called function
    fact = 1

    for i in range(1, num+1):
        fact *= i
    
    print("Factorial of", num , ": ", fact)

fact_cal(5)  # calling function

""" 
> calling function:
   pass the value to called function -> with argument
    here, argument value: 5

> called function:
   receive the value(5) from calling function 
   but no return any value to calling function
"""