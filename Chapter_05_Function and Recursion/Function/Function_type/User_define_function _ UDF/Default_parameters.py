"""  
topic: Default Parameters

obj   : Assigning a default value to parameter.
      -> which is used when no argument is passed

--> NNB:
       when pass argument then must be assign the parameters
                       but
       when does not pass argument then
                                    -> parameter is not assign (we know that)
                                    -> parameter is assign that is possible
                                            --> then must be also assign the values of parameters
                                                details the given example
"""
def sum_cal(num1 = 10, num2 = 20): # but here parameter is assign with value that is completely possible
    sum = num1 + num2
    print(sum)

sum_cal()  # here, no arguments is pass

# parameters must be assign with value
# without assign values is generated error
#    -> def sum_cal(num1, num2) that gives error
