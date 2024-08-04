# Type casting/conversion: -> To convert one type to another type

# > classification of type conversion:
#   -> 1. Implicit type casting
#   -> 2. Explicit type conversion

# > Implicit type casting (Automatic) when working with small-scale data and -scale data.
#   ->  int + int = int
#   ->  int + float = float
#   ->  str * int = str

print("\nExample 1: ")
num1 = 10   # int 
                        # -> o/p: float
num2 = 5.5  # float
sum = num1 + num2
print("Implicit Type Conversion (Automatic): ", sum) # o/p: 15.5
print(type(sum)) # o/p: <class 'float'>

print("\nExample 2: ")

text = "Raihan" # str
                        # -> o/p: str
num = 2   # int
ans = text * num

print("Implicit Type Conversion (Automatic): ",ans) # o/p: RaihanRaihan
print("Type: ", type(ans)) # <str>

# > Explicit type conversion (Manual) when you want to convert a small-scale data to a large-scale data vice-versa
# syntax: target_type(source type)

print("\nExample 3:")
num3 = 20     # source type : int
num4 = float(num3)  # target type: float

print("num4 : ", num4)   # 20.0
print("Type: ", type(num4)) # <float>

print("\nExample 4:")
num5 = 99.99    # source type : float
num6 = int(num5)  # target type: int

print("num5 : ", num6)   # 99
print("Type: ", type(num6)) # int

print("\nExample 5:")
num7 = '100'    # source type : str
num8 = float(num7)  # target type: float

print("num8 : ", num8)   # 100.0
print("Type: ", type(num8)) # float



