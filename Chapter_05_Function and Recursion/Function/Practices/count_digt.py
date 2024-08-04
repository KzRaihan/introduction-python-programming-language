"""   
using UDF, 
Write a program to count number of digits in a given integer
                   and
find the sum of total

"""
def count_digit(num):
    count = 0
    sum = 0

    while(num != 0):
        mod = num % 10
        sum += mod
        count += 1
        num = num // 10
    
    print("Number of Digit: ", count)
    print("Sum of Digit   : ", sum)
    
    

num = int(input("Enter your number: "))
count_digit(num)
