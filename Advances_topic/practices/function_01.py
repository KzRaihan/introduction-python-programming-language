# eg_01:
def number(x):
    return x**2

print(number(8))

def square(f,x):
    return f(x)

print(square(number, 6))

# explanation:
''''
for second function: square
-> first call the square function
-> square function call the number function
-> number function need a argument which is 6 here
'''