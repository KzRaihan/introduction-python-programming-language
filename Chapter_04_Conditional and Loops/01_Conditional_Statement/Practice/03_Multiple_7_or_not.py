# WAP to check if a number is a multiple of 7 or not
# explain: if x is multiple by 7 means -> ( x % 7 == 0 ). modulo or remainder is zero. 

num = int(input("Enter a number: "))
if(num%7 == 0):
    print(num ,"is Multiple by 7")
else:
    print(num,"is not Multiple by 7")
