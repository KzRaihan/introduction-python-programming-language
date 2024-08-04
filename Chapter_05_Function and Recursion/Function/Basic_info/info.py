"""  
Topic: function in python
obj  : Block of statements that perform a specific task

-> syntax:
       # function definition
     def func_name(param1, param2,....):
        --------------------
        --------------------
            statements             this is the body of function
        # some work 
        --------------------
        --------------------
        return value
    
    func_name(arg1, arg2,....)  # calling with argument

--> explain:
     def = keyword
     func_name = similar to variable name
     param1, param2 = parameters 
   
"""
# eg_01:
def cal_sum(num1, num2):  # function definition 
    sum = num1 + num2
    print(sum)

# first time call
cal_sum(6,4)   # <- calling function

# second time call
cal_sum(10, 20) 


""" 
cal_sum = calling function 
          that call the cal_sum function with pass argument 6 and 4


def cal_sum(num1, num2) -> called function

def = keyword
cal_sum = function name
num1 = first parameter (which store the value of 6)
num2 = second parameter (which store the value of 4)

so, 
  num1 = 6
  num2 = 4

-> body:
   sum = num1 + num2
       = 6 + 4
       = 10
    print: 10

when cal_sum is calling with arguments that print the sum of two numbers
"""