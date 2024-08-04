"""  
write a program to check number is armstrong or not.
hint:
    A number is armstrong if the sum of cubes of individual digit of a number is equal to the
    number itself

eg:
    num = 153
    ars_num = 1^3 + 5^3 + 3^3
            = 1 + 125 + 27
            = 153

"""
def armstrong_num(num):
    temp = num
    arm_num = 0

    while(num != 0):
        mod = num % 10
        arm_num += mod*mod*mod
        num //= 10
    if(temp == arm_num):
        print(temp,"is the armstrong number")
    else:
        print(temp, "is not armstrong number")

num = int(input("Enter your number: "))
armstrong_num(num)