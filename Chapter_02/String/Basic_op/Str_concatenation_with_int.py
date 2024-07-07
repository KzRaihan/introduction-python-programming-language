# String can be multiplication(*) with numerical(int) value.
# only int value is multiplication with string

# eg_01
Str1 = "Kz"
num1 = 3

mult1 = Str1 * num1

print("Result1: ", mult1)   # mult1 =KzKzKz (Kz in 3 times)

# eg_02

str2 = "Kz"
num1 = 5

mul = str2 * num1

print("Result2: ", mul)  #  Kz is 5 times

# eg_03
str1 = "Kz"
str2 = "Ra"

concat = str1 + str2  # Kz + Ra = KzRa

multiple = concat * 2

len1 = len(concat)   # len1 = 4 (KzRa)
len2 = len(multiple) # len2 = 4*2 

print("\nLength of ",concat, "is: ", len1)   # 4

print("Multiplication str and int: ", multiple) # KzRa is 2 times
print("Length of ",multiple,"is : ", len2) # 8
