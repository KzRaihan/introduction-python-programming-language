"""   
Topic : range() function
obj   : return the sequence of numbers

-> 2. star, stop values(points)

-> syntax: 
       range(start_value, stop_value)

       -> start_value = enter by user
       -> stop_value  = enter by user
       -> step size   = always increment by one (by default) -> it is not decrement 
    eg:
      range(2, 10)
       here, 
             2 = start value
             10 = stop value 
"""
print("Example one: print 5 to 50 ")

for i in range(5, 51):  # why 51 => stop val is not included for print
    print(i)

print("\nexample two: print 100 to 1000")

for j in range(100, 1001):
    print(j)
