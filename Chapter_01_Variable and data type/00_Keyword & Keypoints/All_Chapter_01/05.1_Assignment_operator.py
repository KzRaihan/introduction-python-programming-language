# Assignment Operator: assign(assign with increment, decrement, mul, div, etc) the value on the right to the variable on the left

# 1.simple assignment (=):

num1 = 10 - 5         # num1 = 10 - 5                             # here,  num1    => operand
                      #      => 5                                 #         '='    => operator
                      #  5 is assign in num1 variable
print("\n1. Simple assignment: ",num1) # o/p: 5

# 2. Addition assignment (+=):
num2 = 6
num2 += 4          # num2 = num2 + 4
                   #      => 6 + 4 
                   #      => 10
 
print("\n2. Addition Assignment: ",num2) # o/p: 10

# 3. Subtraction assignment (-=):

num3 = 15
num3 -= 10         # num3 = num3 - 10
                  #      => 15 - 10 
                  #      => 5
print("\n3. Subtraction Assignment: ", num3)

# 4. Multiplication assignment (*=):

num4 = 10
num4 *= 3          # num4 = num4 * 3
                   #      => 10 * 3 
                   #      => 30
print("\n4. Multiplication Assignment: ", num4)

# 5. Division assignment (/=):

num5 = 30
num5 /= 2          # num5 = num5 / 2
                    #      => 30 / 2 
                    #      => 15.0
print("\n5. Division Assignment: ", num5)

# 6. Floor division assignment (//=):

num6 = 15
num6 //= 2         # num6 = num6 // 2
                    #      => 15 // 2 
                    #      => 7
print("\n6. Floor Division Assignment: ", num6)

# 7. Modulus assignment (%=):

num8 = 20
num8 %= 3          # num8 = num8 % 3
                    #      => 20 % 3 
                    #      => 2
print("\n7. Modulus Assignment: ", num8)

# 8. Exponentiation assignment (**=):

num7 = 2
num7 **= 2         # num7 = num7 ** 2
                    #      => 2 ** 2 
                    #      => 4
print("\n8. Exponentiation Assignment: ", num7)
