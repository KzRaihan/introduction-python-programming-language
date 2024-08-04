"""  
topic: user definition function (UDF)
obj  : UDF is create by the programmer

> benefit: 
   -> make the code reusable
                    (declare them once and use them multiple times)
   -> make the program easier
               (each task divided into smaller task) 
    
   -> increase readability


> syntax:
      
     def func_name(param1, param2,...): -> function definition with parameters
        -------------------------
        ------statements---------    -> body of function
        ------ works -------------

        return work_value

    func_name(arg1, arg2,...)  -> this the function calling with argument

   >> arguments  = pass the values to parameter
   >> parameters = catch the values from argument

   >> function calling : 
     while creating any function, that give a definition of what the function has to do.
     To use a function, we will have to call that function.
"""
# eg_01: create a user definite function

# function definition with no parameters
def cla_mul():
    num1, num2 = 2,3
                                    
    mul = num1 * num2                   # work 
    print("Multiplication: ", mul)

cla_mul() # <- function calling with no passing argument

# eg_02: create UDF to calculate factorial of a number

# function definition with one parameter
def fact_cal(val):
    fact = 1
    for i in range(1, val+1):
        fact *= i 

    return fact

print(fact_cal(5)) # <- fact_cal() function calling with one argument which is: 5
