# Tuples method or function:
# tuples function can't change the old tuple because it's immutable
# when performs any methods tuple then it will return new tuple 

print("\nExample 1: concatenation ")

tup = ()     # empty tuple
tup_01 = ("Kz", 20, 30, "Raihan", 100.00)

# concatenation
add_tup = tup + tup_01

print(add_tup)    # output: ('Kz', 20, 30, 'Raihan', 100.0)

# repetition
print("\nExample 2: Repetition")


repeat_tup = tup_01 * 2
print(repeat_tup)    # output: ('Kz', 20, 30, 'Raihan', 100.0, 'Kz', 20, 30, 'Raihan', 100.0)

# tup.index(el) : -> return the idx of first occurence 
                    # if element is not found it will throw ValueError

print("\nExample 3: index(el) ")

print("First idx of 'Raihan' element: ", tup_01.index('Raihan'))    # output: 3
# print("idx of zero element : ", tup_01(0))   #    o/p: Error

# Example 3.  tup.count(el) : -> return the count of el in tuple
print("\nExample 4: count(el)")
print("Raihan element are: ", tup_01.count("Raihan"))   # o/p: 1

# Example 4. min(tup_name) and max(tup_name):
print("\nMin and Max function: ")
val = (10, 20, 30, 40)
small_val = min(val)
big_val = max(val)

print("\nSmall value : ", small_val)
print("\nBig value   : ", big_val)