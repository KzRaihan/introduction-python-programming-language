# Logical operator

# 1. Logical 'and': -> Return True if both conditions are True 
                  # -> Return False if at least one cds is False 
print("\n1. Logical AND operator: ")
# eg_01
num1 = 10
num2 = 0
                                      # if one value is False then return the False value
                                      # if two value is true then return the last variable value
num3 = num1 and num2                  
print("\nEg_01: ",num3)  # 0 <- zero is False that way, return the False value

# eg_02
num4 = 20
num5 = num1 and num4   # in this time return the last variable value because two value is true

print("\nEg_02: ",num5) # 20

# eg_03
print("\nEg_03")

print(True and True) # True
print(False and True) # False


# 2. Logical 'or' operator:
       # -> Return True if at least one condition is True.
       # -> Return False if both conditions are False.

# eg_01
print("\nExample 1: ")

print(True or False) # True
print(False or False) # False

# eg_02

print("\nExample 2: ")

num6 = 20
num7 = 0
num0 = False

ans = num6 or num7           # here, num6 => 20 (True), num7 => 0 (False)
                             #    True or False => o/p: True 

print("Example two: ", ans) # 20  -> Return 'True' if at least one condition is True.
print(num0 or num7)         # 0   -> Return 'False' if the both cds is False



# 3. Logical 'not' operator: -> Return True if the condition is False vice-versa
print("\nExample 3:Logical not operator ")

print(not True) # False

print(not False) # True

print(not 0) # True

print(not 1) # False

var1 = 10
var2 = 0

ans = not var1    # not True
                  # False 
answer = not var2

print("\nans: ", ans)  # False
print("answer: ", answer) # True