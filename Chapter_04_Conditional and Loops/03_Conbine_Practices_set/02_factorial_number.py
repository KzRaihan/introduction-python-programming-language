# WAP to find the factorial of first n numbers

num = int(input("\nEnter your number: "))

fact = 1
i = 1

while(i<=num):
    fact *= i
    i += 1
print(f"\n{num} factorial is : {fact}")


# using for loop
fact1 = 1
for k in range(1,num+1):
    fact1 *= k

print(f"\n{num} factorial using for loop is : {fact1}")