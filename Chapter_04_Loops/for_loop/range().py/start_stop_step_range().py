"""   
Topic : range() function
obj   : return the sequence of numbers

-> 3. star, stop, step_size values(points)

-> syntax: 
       range(start_value, stop_value, step_size)

       -> start_value = enter by user
       -> stop_value  = enter by user
       -> step size   = enter by user (which is increment and decrement)
    eg:
      range(2, 20, 2)
       here, 
             2  = start value
             20 = stop value
             2  = increment value

"""
print("Example one: print 1 to 15")

for i in range(1, 16, 1):  # stop value is not include for print
    print(i)

print("\nExample two: print all odd numbers form 1 to 100 ")

for j in range(1, 100, 2):
    print(j)

print("\nExample three: print even number form 100 to 1")

for k in range(100, 0, -2): 
    print(k)
