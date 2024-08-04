"""  
WAP to check whether a number is palindrome or not
hint: A number is palindrome if we reverse it . it will not change
 eg: 
  num = 121
  reverse_num = 121
"""
def check_palindrome(num): # called function
    temp = num
    reverse_num = 0

    while(num != 0):
        mod = num % 10
        reverse_num = reverse_num * 10 + mod
        num = num // 10
    
    if(temp == reverse_num):
        print(temp , "is Palindrome")
    else:
        print(temp, "is not palindrome")

num = int(input("Enter your number: "))

check_palindrome(num)  # calling function
