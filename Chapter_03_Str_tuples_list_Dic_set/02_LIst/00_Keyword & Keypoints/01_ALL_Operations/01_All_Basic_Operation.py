# list : A built in data type that stores set of values.
#        -> list are mutable (values can be modify or changeable)
#  Syntax : 
#       list_name[values,...]

# example: 1. same values 
print("\nExample 1: Same values ")
str1 = ["Kz", "Raihan", "Rahim", "Rashel", "Shajib"]   # here all string values

print("Values of list str1 are: ", str1)
print("Type_str1: ",type(str1))   # < list >

# example: different values
print("\nExample 2: Different values ")

str2 = ["Kz", "Raihan", 4039, 98.89]  # here int and float values
print("\nValues of list str2 are: ", str2)
print("Type_str2: ", type(str2))  # <list>

# 3. example: nested list
print("\nExample 3: Nested list")

str3 = ["Kz", "Raihan", ["Dhaka", "Chittagong", "Sylhet"], 98.89]
print("\nValues of list str3 are: ", str3)
print("Type_str3: ", type(str3))  # <list> 

# 4. list value can be changeable or modify
str2[2] = 4040
print("Modify the value then list(str2): ",str2)

# 4. example: slicing of list  -> Access part of list or sublist
print("\nExample 4: Slicing of list")

country = ["Bangladesh", "America", "Russia", "China", "Canada", "France", "Spain", "Italy", "Finland", "Germany", "South Korea", "Japan", "Saudi Arabia"]
print("\nCounties: ", country)
print("Type", type(country))

# idx -> 0 to 6

sliced_country = country[0:7]
print("\nSliced Countries: ", sliced_country)

# skip some countries

sliced_country_2 = country[::2]    # skip counties 2 | because here step size 2 
print("\nSliced Countries (every second country): ", sliced_country_2) 

# eg_02
list = [10, 20, 30, 40, 50]
neg_step = list[3:0:-1]
print(neg_step)


