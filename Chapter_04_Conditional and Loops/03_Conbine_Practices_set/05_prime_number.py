# WAP to find whether a given number prime or not.
# hint: 1 and given number is not count

num = int(input("\nEnter your number: "))

flag = 0

for i in range(2,num):
    if(num%i ==0):
        flag = 1
        print(f"{num} is not prime")
        break

if flag == 0:
    print(f"{num} is prime")