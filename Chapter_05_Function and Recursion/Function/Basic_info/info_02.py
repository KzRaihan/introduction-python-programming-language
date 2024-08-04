"""  
Topic: Function

syntax:
   def fun_name(parameters):
    -------------------
    ----statements----
    --------(work)-----
    
    return work value

    # function calling
    fun_name(arguments)

def means = function definition
parameters = function input values
           -> the part which is present in function definition unit

arguments = the part which is present in function calling with passing values 

"""
# eg_01 : create a function that do sum of three numbers

# Function definition part

def sum_cal(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum


# function calling with three arguments
result = sum_cal(10, 20, 30) 

print(result) # 60

""" 
10 is store by num1
20 is store by num2
30 is store by num3

return the sum in sum_cal function
result is store the value of sum_cal
"""