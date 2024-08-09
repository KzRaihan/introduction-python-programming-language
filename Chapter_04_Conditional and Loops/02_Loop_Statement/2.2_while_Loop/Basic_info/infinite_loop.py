"""  
Topic: infinite loop

    >> infinite loop is very dangerous
    >> not use in professional and practical life

-> There are many way to create an infinite loop
   >> loop counter is decrement when ending value is bigger than smaller value
       
"""
# eg_01 : loop counter is decrement
i = 2
while i < 10:
    print("Welcome")
    i -= 1

# eg_02: when single value is loop counter is True
while True:
    print("Hello")

# eg_03: when single value is non zero
while(1):  # here, -2, -50, 5, 10 , True(any non zero values and boolean value False)
    print("Good Bye")
