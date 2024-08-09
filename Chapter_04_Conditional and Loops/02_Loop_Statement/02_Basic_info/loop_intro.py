"""   
topic: loops in python
obj  : Repeat block of code, until a specified condition is met.
      -> loops are used to repeat instructions

type:
     loops are two type in python
       >> while loop
       >> for loop
"""
# eg_01: print 5 times hello

# First way
print("In general way to print hello 5 times: ")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello\n")

# Second way using loop
print("\nUsing loop to print hello 5 times: ")
i = 1
while(i<=5):
    print("hello")
    i += 1
# print 1 to 5
print("\nIn general way to print 1 to 5 : ")
print(1) 
print(2) 
print(3) 
print(4) 
print(5) 

# Second way : using loop
print("\nUsing loop to print 1 to 5 : ")
j = 1
while j <= 5:
      print(j)
      j += 1
