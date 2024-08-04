""" 
WAP to find the factorial of first n numbers.

i/p : 4

fact = 1 * 2 * 3 * 4
     = 24
or, 
fact = 4 * 3 * 2 * 1
     = 24
"""
num = int(input("Enter any integer: "))
fact = 1
for i in range(1,num+1, 1):
    fact *= i

print("Factorial of ", num, "is: ", fact)

# for i in range(1, num+1):
#     fact *= i
# print(fact)

""" 
                 code explain

-> i/p: 
    num = 4

-> for loop:
    start: 1
    stop : num + 1
         =  4 + 1
         =  5
    step size = 1

    1st iteration:
    -------------
    start : 1

    loop : i in range 1
           => i = 1
      body: 
           fact = fact * i
                = 1 * 1
                = 1
    inc: i = 1 + 1
           = 2
    2nd  iteration:
    -------------
    start : 2

    loop : i in range 2
           => i = 2
      body: 
           fact = fact * i
                = 1 * 2
                = 2
    inc: 
        2 + 1
        = 3

    3th  iteration:
    -------------
    start : 3

    loop : i in range 3
           => i = 3
      body: 
           fact = fact * i
                = 2 * 3
                = 6
    inc: 
      3 + 1
      = 4
    4th  iteration:
    -------------
    start : 4

    loop : i in range 4
           => i = 4
      body: 
           fact = fact * i
                = 6 * 4
                = 24
    inc: 
      4 + 1
      = 5
     here i became 5 so stop condition full 

     

"""