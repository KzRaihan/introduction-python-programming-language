# Tuple : A built in data type that store set of values
#      -> values can be similar and different
#      -> It is immutable data type

# Syntax: tuple_name(values)

# Example_01: same values
print("\nExample 1: ")

tup = ("Kz", "Raihan", "Dhaka", "Bangladesh")

print("Tuple values: ", tup)
print("Type: ", type(tup))   # <tuple>

# Example_02: different values
print("\nExample 2: ")

values = ("Hello", 90, 99.99, True)
print("\nValues: ", values)
print("Type: ", type(values))

# Example_03: empty tuples
print("\nExample 3: ")

empty_tup = ()
print("Empty: ", empty_tup)
print("Type: ", type(empty_tup))


# Example_04: single(only one) values in tuples
print("\nExample 4: ")

tup_01 = ("Kz")  # this is not valid syntax it is count as string data type
tup_02 = ("Kz", ) # this is the valid syntax to assign single value and it's count tuple

print(f"\nSingle value in tuples:{tup_01, tup_02}")


print("Type: ", type(tup_01), type(tup_02))   # <class'str'> and <class 'tuple'>

# Example_05 : Indexing: -> Access a Specify or individual elements within tuples 
#                        -> Can't modify the values of tuples

print("\nExample 5: ")

tup_03 = (10, "Kz", 99.999, True, "98", 100)

print("First element: ", tup_03[0])     # 10
print("Four element: ", tup_03[3])      # True
len1 = len(tup_03)
print("Last element: ", tup_03[len1-1]) # 100

# Example_06: Tuple slicing : -> Access of part of the tuple.

print("\nExample 6: ")

print("Slicing values from 1 to 3: ", tup_03[1:4])  # ('Kz', 99.999, True)

reverse = tup_03[::-1]
print("Reverse tuples: ", reverse)


# Example 7: tuple all values stores in single variable
print("\nExample : 7 ")
val = (10, 20, 30, 40)

num1, num2, num3, num4 = val
print("num1: ", num1)
print("num2: ", num2)
print("num3: ", num3)
print("num4: ", num4)


   