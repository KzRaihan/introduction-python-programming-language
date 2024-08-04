""" 
Topic: range() function
obj  : return a sequence of numbers

-> syntax:
        range(start?, stop, step?)
        --> here,
              start = 0 (By default) this optional
              stop  = a specific number(given by user) mandatory
         step size  = 1 (By default) increment

-> type: three
   --> 1. only stop point:
   --> 2. start, stop points
   --> 3. start, stop, step size points
    
     
-> 1. only stop point:
    syntax :
          range(3)  when assign only one value it count stop point
          -> return 0 1 2  
          -> range() start with 0 and increment by 1 for single or stop value
          -> stop value is not include
          -> it is not decrement , always increment by one. 
  
"""
print("example one: in general print")

seq = range(5)

print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

print("\nType: ", type(seq)) # this is range type


print("using for loop with single value in range")

for val in seq:
    print(val)
print(type(val))

print("\nExample two: print 2 to 15")

for i in range(16):  # 16 why? => because stop value is not include
    print(i)

print("example three: print 1 to 10")
for j in range(10):
    print(j+1)
   
