""" 
Topic : Function argument and return values UDF categorizes 
>> Function with
    -> 1. no arguments and no return value
    -> 2. no arguments and a return value
    -> 3. With arguments and no return value
    -> 4. With arguments and a return value

> 1. no argument and no return value:
  -> no argument:
               Called Function does not receive any data from calling function
               -> calling function does not pass any data 
  -> no return:
               calling function doesn't receive any data from the called function
               -> called function does not return any data
"""

# eg_01: no arguments and no return value -> calculate modulo of a number
def mod_cal(): # <- called function
  num = 11 % 2
  print("modulo: ", num)

mod_cal() # <- calling function


"""  
      code explain

here, calling function is no argument passing to called function
       -> mod_cal() 
      
      called function is no parameter catch from calling function
        -> def mod_cal()
"""