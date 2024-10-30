def equation(x,y):
    x = (x**2) + (4*x) - 3   # x = 3^2 + 4*3 -3 => 9 + 12 - 3 => 18
    y = (y**3) + (4*y) + 6   # y = 2^3 + 4* 2 + 6 => 8 + 8 + 6 => 22

    z = x + y  # 18 + 22 => 40
    print(z)  # o/p: 40
    return

equation(3,2) # o/p: 40

# example two
def num(x, y= 50):
    print(x, y)

num(10,30)

# example three
def cal_equ(x, y):
    y = 10
    x = x + 10
    y = y - 10
    z = x * y

    return z

ans = cal_equ(10, 5)
print(ans)

# example four: variable length argument

def calculate(x, *p): # here, catch the value 
    total = x - 3
    print("Total: ", total)
    # print("Type: ", type(p))

    for i in p:
        print(i)
    return

calculate(1000, 10, 20, 30, 40, 50)

# example five : pass by reference
lst = [1, 2, 3, 4]

def fun_num(x, y):
    print(x)

    for i in y:
        print(i)
    return

fun_num(lst, [10, 20, 30, 40])
