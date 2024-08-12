# WAP to print the multiplication table of a given number 

num = int(input("Enter your table number: "))

i = 1
while (i<=10):
    print(f"{num} X {i}: {num * i}")
    i += 1

print(f"\nTable {num} using for loop : ")
# using for loop

for k in range(1, 11):
    print(f"{num} X {k}: {num * k}")
    
