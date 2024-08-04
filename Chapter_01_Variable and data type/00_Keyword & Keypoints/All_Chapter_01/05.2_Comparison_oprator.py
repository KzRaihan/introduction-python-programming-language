# Comparison operator:  Return the value always is boolean data type
# use : conditions statements very useful.

# 1. Equal to (==):
print("\n1. Equal to operator")

num1 = 10
num2 = 10

print(num1 == num2) # o/p: True

num3 = 30
print(num1 == num3) # o/p: False

# 2. Not equal to (!=):
print("\n2. Not Equal to operator")

print(num1 != num2) # o/p: False
print(num2 != num3) #o/p: True

# 3. Greater than(>): -> check if the left(first value) op is greater than the right(second value) op
print("\n3. Greater than operator")

val1 = 50
val2 = 20

print(val1 > val2) # o/p: True
val3 = 50

print(val1 > val3) # o/p: False

# 4. Greater than or equal(>=): -> check if the left(first value) op is greater than or equal the right(second value) op
print("\n4. Greater than or equal operator")

val1 = 50
val2 = 20

print(val1 >= val2) # o/p: True
val3 = 50

print(val1 >= val3) # o/p: True

# 5. Less than(<): -> check if the left(first value) op is less than the right(second value) op
print("\n5. Less than operator")

var1 = 10  # left or first value
var2 = 20  # Right or second value
var3 = 10  # Right or second value

print(var1 < var2) # o/p: True
print(var1 < var3) # o/p: False

# 6. Less than or equal(<=): -> check if the left(first value) op is less than or equal the right(second value) op
print("\n6. Less than or equal operator")

var1 = 10 <= 20 # this statement is True
var2 = 0        # zero(0):-> False statement
var3 = 5        # 5 means : True

print(var1 <= var2) # True <= False            # True is Less than False -> no | False
                    # o/p: False               # True is equal to False -> no | False

print(var1 <= var3) # True <= True
                    # o/p: True

