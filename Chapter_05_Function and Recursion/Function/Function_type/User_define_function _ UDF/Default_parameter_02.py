""" 
Topic: Default parameters
obj  : Default values is always assign(store) the last parameters

-> syntax:
       def func_name(non_default_parameter, ..., default_parameter=value)
"""

print("\nExample one: ")

def cal_prod(num1, num2 = 2):
    print("num1: ", num1)
    print("num2: ", num2)

    print("Product: ",num1 * num2)

cal_prod(5) # calling function

"""  
num1 = (5) -> store the value of the pass argument
num2 = (2) -> default parameter store the value which is the assign 
"""

# def div_cal(num1 = 9, num2):
#     div = num1/num2
#     print(div)

# div_cal(3)  -> this is generate by error
# because first parameter is non default and last parameter is default
#     -> but here first parameter = default 
#     ->  last parameter  = non default    -> this is the wrong syntax of default parameter

