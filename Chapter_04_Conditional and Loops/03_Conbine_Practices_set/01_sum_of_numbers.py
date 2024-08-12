# WAP to find the sum of first n (natural) numbers

num = int(input("Enter your number: "))

# using while loop
i = 0
sum = 0

while (i<=num):
    sum += i
    i += 1
print(f"\nsum of first {num} numbers: {sum}")

# using for loop
sum1 = 0
for k in range(0,num+1,1):
    sum1 += k
print(f"\nsum of first {num} numbers: {sum1}")

