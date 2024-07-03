"""
  An operator is a symbol that perform a certain operation between operands.

"""
# Arithmetic operator

# 1.Addition op(+):
num1 = 10
num2 = 20

add = num1 + num2
print("Addition of two numbers :", add)

# 2. Subtraction op(-):
num1 = 20
num2 = 10

sub = num1 - num2  # sub = 20 - 10
                   # sub = 10
print("Subtraction of two numbers :", sub)

# 3. Multiplication(*):
num1, num2,num3 = 2,4,6

mul = num1* num2 * num3   # mul = 2 * 4 * 6
                          # mul = 8 * 6
                          # mul = 48
print("Multiplication of three numbers :", mul)

# 4. Division(/):
num1,num2 = 10,2

div = num1/num2     #   2) 10 (5 <- this is the division answer
                    #      10
                    #      --
                    #       0
print("Division of two numbers :", div)

# 5. Floor Division (//) or integer Division:
#   >> when result is float then the final result gives closest integer, which is lesser than or equal to the float value.
# eg: 
# result come : 7.5 then final result : 7
# result come : 1.6 then final result : 1

# case_01: int and float(vice versa) then result will float

num1 = 1.5
num2 = 3

int_div = num1//num2     #  3 ) 1.5 ( 0.5 <- this is the result but this convert into closest integer which is 0(less than or equal the 0.5) and 0(int) is convert float(0.0)
                         #      1.5
                         #      ----
                         #       0       
print("Floor Division of two numbers :", int_div) # 0.0

# case_02: int and int then result will int
num1 = 12
num2 = 5

int_div_1 = num1//num2     #  5 ) 12 ( 2.4 <- this is the result but this convert into closest integer which is 2(less than or equal the 2.4)
                           #      12
                           #     -----  
                           #       0     
print("integer division of two numbers: ", int_div_1) # 2

# case_03: Neg_int and int but result will come float then the final result is covert to integer which is less than or result
num1 = -12
num2 = 5

int_div_2 = num1//num2     # -3 ) -12 ( -2.4 <- this is the result but this convert into closest integer which is -3(less than or equal the -2.4)
                           #      -12
                           #      -----
                           #       0
print("neg_int and int integer division: ", int_div_2)


# 6. modulo or remainder(%):

num1, num2 = 10, 3        # 3) 10 ( 3
                          #     9
                          #    ---
                          #     1 <- this is the modulo or remainder
mod = num1 % num2
print("Modulo :", mod) # 1

# 7. Exponentiation (**):
num1 = 10
num2 = 2

power = num1 ** num2  #  10^2 = 100

print("Exponentiation :", power) # 100


