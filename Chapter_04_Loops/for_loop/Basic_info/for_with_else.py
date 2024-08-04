""" 
Topic: else in loop
obj  : this is optional 
    -> to check loop is fully(complete) run(execution) or not.
    -> if loop is complete work then else part is execution

    -> syntax:
         for el in list:
            # some work
         else:
            # work when loop ends 
"""
print("Example one: ")

list = [10, 20, 30, 40]

for el in list:
    print(el)
else:                 # here, loop is complete work
    print("loop end")
    
print("\nExample two: ")

str = "Md Kamruzzaman Raihan"

for char in str:
    if(char == 'r'):
        print("r is found")
        break
    print(char)
else:
    print("Loop end")  # here, loop is't complete(for break statement) so, else part is not work


print("\nExample two: when use continue statement")

list = [1, 3, 5, 7]

for el in list:
    if el == 5:
        # print(el)
        continue  # only one value is not work 
    print(el)     # but complete loop is work
else:
    print("loop end") # that way, this else part is work
    