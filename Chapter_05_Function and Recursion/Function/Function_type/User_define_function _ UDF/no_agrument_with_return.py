"""  
Topic: function 
obj  : no argument and a(with) return value

-> no argument:
  called function doesn't receive any data from calling function
    --> calling function does not pass any data

-> with return:
  calling function receive data from the called function
    --> called function return the values to calling function

"""
# called function with return value
def even_odd():
    num = int(input("Enter any integer: "))

    if(num%2 == 0):
        print("Even number: ", end = " ")
        return num
    else:
        print("Odd number: ", end = " ")
        return num

result = even_odd()  # <- calling function  with no argument
print(result)   

""" 
called function:
      -> does not receive any data form calling function this known as no argument
      -> but here, def even_odd() return the value to calling function this known as a return value
calling function:
      -> does not send(pass) any data to called function this known as no argument
      -> but here, even_odd() receive the value from the called function this know as a return value
"""