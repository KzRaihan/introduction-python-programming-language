"""  
topic: while loop in python 
obj  : 

Syntax: 
     initialization
     while (condition):
        -------------
        -------------
        Do somethings if cds is true
        ---------------------------
        update(increment/decrement)


  --> initialization:
      starting points(loop start point)

  --> condition:
      termination condition
      starting points and ending points
  
  --> update:
       init values is update here
       two type:
            increment: to increment the init value
            decrement: to decrement the init value
      
"""
# print 10 times of hello
print("\nExample one print 10 times Hello with count iteration: ")
i = 1      # init 
while(i<=10):      # cds
    print("Iteration: ", i)
    print("Hello") # work
    i += 1 # update(increment)

# print 10 to 1 
print("\nExample two print 10 t0 1: ")
j = 10 # init
while j >= 1: # cds 
    print(j)  # work
    j -= 1    # update(Decrement)
