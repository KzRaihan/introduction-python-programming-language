# WAP to print the multiplication table of a given number using for loops in reversed order.

num = int(input("Enter your table number: "))

for k in range(10, 0,-1):
    print(f"{num} X {k}: {num * k}")
    
