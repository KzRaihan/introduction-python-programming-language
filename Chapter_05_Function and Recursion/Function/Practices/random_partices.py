"""   
using UDF, 
Write a program to count number of digits in a given integer
                   and
find the sum of total

"""

num = int(input("Enter number: "))

count = 0
T_sum = 0


while(num != 0):
    mod = num % 10
    T_sum += mod
    num //= 10
    count += 1

print("Number of digit: ", count)
print("sum of number : ", T_sum)
