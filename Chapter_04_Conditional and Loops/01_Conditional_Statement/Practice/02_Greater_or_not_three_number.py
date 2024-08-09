# WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))
if(num1 == num2 == num3):
    print("The Numbers is same")
elif((num1>=num2) and (num1>=num3)):
    print("First is greatest number: ",num1)
elif((num2>=num3)):
    print("Second is greatest number : ",num2)
else:
    print("Third is greatest number : ", num3)
