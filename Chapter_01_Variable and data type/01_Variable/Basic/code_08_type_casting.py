'''
  -> Type casting of variable
    
    >> To converting a variable from one data type to another.
    
    >> The two main types of type casting.
       1. Implicit Type Conversion (Automatic)
            -->  Python automatically converts one data type to another.(smaller type convert to bigger type).
       2. Explicit Type Conversion (Manual)
            --> User can only convert  Manually in code.
            --> syntax: 
                      target data type(source variable name)


'''
print("Implicit Type Conversion (Automatic)")

num1 = 49.59
num2 = 50

print("Sum = ", num1 + num2)  # num2 to convert to num1 type.|| op: Sum = 99.59

print("Explicit Type Conversion (Manual)")

num1 = 49.59
num2 = 50
g = 9.8
name = "python"
price = 550
nm = '10'

# Convert int to float
print("num2 = ", float(num2)) # op: num2 = 50.00

# Convert float to int
print("num1 = ", int(num1)) # op: num1 = 49

# Convert float to int
print("g = ", int(g))  # op: g = 9

# Convert int to string
print("num2 = ", str(num2)) # op: num2 = 50

# Convert string to int
print("name = ", str(nm))  ## op: name = 10 (less effective)