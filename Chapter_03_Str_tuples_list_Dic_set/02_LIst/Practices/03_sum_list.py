# WAP to sum a list with 4 numbers

# eg_01
print("\nExample 1: ")
nums = [10, 20, 30, 40]
print(sum(nums))  # sum() return the sum of all values of nums(list)

print("\nExample 2: Numbers input from user ")
num1 = []

val1 = int(input("Enter first number: "))
num1.append(val1)

val2 = int(input("Enter 2nd number: "))
num1.append(val2)

val3 = int(input("Enter 3th number: "))
num1.append(val3)

val4 = int(input("Enter 4th number: "))
num1.append(val4)

ans = sum(num1)    # means -> summation of all num1 values/elements

print("\nSum of all element of num1: ", ans)