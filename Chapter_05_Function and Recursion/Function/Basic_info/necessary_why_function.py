"""  
Topic : Necessary of function
obj   : To remove the repeat or redundant code.
       
      -> reusable and readability

"""
# eg_01: summation of two numbers
print("\nWithout function to print two numbers: ")
num1 = 10
num2 = 5

sum = num1 + num2
print(sum) # 15

# more lines of code(assume that 1000)
# then we need to again perform summation of two numbers
num1 = 30
num2 = 20

sum = num1 + num2
print(sum) # 50


# more lines of code(assume that 2000)
# then we need to again perform summation of two numbers
num1 = 60
num2 = 40
sum = num1 + num2
print(sum) # 100

# more lines of code(assume that 3000)
# then we need to again perform summation of two numbers 
# what happen???

"""
>> the same code is perform again and again as require by project
>> if we can write again and again that is not problem but not a good solution
>> A good programmer this type of problem solve by function
   -> when repeat or redundant code present

"""
# eg_02: using function to solve this problem in effective way

print("\nWith function to print two numbers: ")

def cal_sum(num1, num2):
    sum = num1 + num2
    print(sum) # print
    return sum # return 

# first time call
cal_sum(10, 5) # 15
# second time call
cal_sum(30, 20) # 50
# third time call
cal_sum(60, 40) # 100

# if we try to ask by user
print("\ninput from user: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = cal_sum(num1, num2) # calling function with arguments and store the return value in result variable
print(result)   # print the result value
