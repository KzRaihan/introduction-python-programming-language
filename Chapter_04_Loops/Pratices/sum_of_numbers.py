"""  
WAP to find the sum of first n numbers

i/p:
   n = 4
sum = 1 + 2 + 3 + 4
    = 10
"""
num = int(input("Enter number: "))

sum = 0

for i in range(1, num+1, 1):  # if step size 1 is optional this question
    sum += i

print("summation of 1 -",num, "numbers: ",sum)
