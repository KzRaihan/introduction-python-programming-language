""" 
Topic: UDF categories
obj  : with argument a return value

with argument:
     called function received data from the calling function

with return:
     calling function receive data from the called function
     called function return(send) value to calling function
"""
# called function with receive three values
def cal_avg(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum/3

    return avg

val1 = int(input("Enter First number : "))
val2 = int(input("Enter second number: "))
val3 = int(input("Enter Third number : "))

print("\nFirst time called for input values: ")
result = cal_avg(val1,val2, val3)    # <- calling function with pass three arguments
print("Average of there numbers: ", result)

print("\nSecond time called for Direct values: ")
ans = cal_avg(10, 20, 30) # <- second time calling function call the called function and pass three arg(10, 20, 30)
print("Answer: ", ans)

print("\nThird time called for Direct values and direct print: ")
print("Average : ",cal_avg(5,7,9)) # third time call