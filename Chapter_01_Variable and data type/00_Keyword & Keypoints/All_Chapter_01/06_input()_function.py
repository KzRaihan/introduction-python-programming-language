# input() : used to accept values(data) using keyboard form user.
#        -> all input form user count as string data type then as need we type conversion/casting the require data type

# Syntax: input("Enter Message or passing string")

# eg_01

name = input("Enter Your name: ")

print("Name is : ", name)

# eg-02 : input form user as integer value

num = int(input("Enter any integer: "))             #  we can't enter any float or other data type
                                                    # it can provide error
print("Number is : ", num)

# eg_03 : input form user as float value

price = float(input("Enter book price: "))

print("Price is : ", price)

