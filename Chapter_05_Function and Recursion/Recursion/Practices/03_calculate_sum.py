# WARF to calculate the sum of first n natural numbers.

def cal_sum(num):      # Recursive function
    if(num == 0):      # Base case or stop cds
        return 0
    else:          # works
        sum = cal_sum(num-1) + num          # return num + cal_sum(n-1)
    return sum



num = int(input("Enter Your number: "))

catch = cal_sum(num)   # calling function
print(f"sum of first {num} is : {catch}")
