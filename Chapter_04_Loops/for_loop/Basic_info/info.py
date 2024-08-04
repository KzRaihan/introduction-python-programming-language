""" 
Topic: for loop 
obj  : loop are used for sequential traversal.
     -> for traversing 
         --> string
         --> tuples
         --> list  etc which has idx(linear sequences)
    
    -> syntax:
        for el in list:      # list all elements are one by one assign el variable
            ----------
            some work        # body of for loop
            ----------
            ----------
      
      # here, 
          for = keyword
          in  = keyword
          el  = general variable which are contains all list values(not idx)
         list = any linear or sequence data structure     
       
        
    
"""
print("Example one: integer list elements traversal or print")

list = [1, 2, 3, 4]  # this is list

for el in list:   # for loop -> here, el is contains values of list not idx
    print(el)

print("\nExample two: string element traversal and access")

str = "Kz_Raihan"  # str is a string 

for char in str:   # char = simple variable
    print(char)

print("\nExample three: tuples element traversal and access")

tup_val = ("Potato", "Tomato", "Ladyfinger", "Cucumber")

for val in tup_val:  # val is variable that can contains all tup_val elements one by one.
    print(val)

