"""  
WAP to input numbers range and store in list and print 
"""
list = []

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# store the numbers in list
for num in range(num1, num2+1):
    list.append(num)

# output the numbers
print(list)
