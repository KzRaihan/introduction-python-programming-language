# Operator: An operator is a symbol that perform a certain operation between operands

# Syntax:   operand < operators > operand             # here operand = all variables, numbers
# Types of operators:
#   -> 1. Arithmetic operator
#   -> 2. Assignment operator
#   -> 3. Comparison/Relational operator
#   -> 4. Logical operator

print("\nArithmetic Operator: ")

# 1. Addition (+):
num1 = 15
num2 = 4
                                                  
sum = num1 + num2  # sum =  15 + 4                 # num1, num2 => operand
                   #     => 19                     #     +      => operator

print("\nAddition: ", sum) # o/p: 19

# 2. Subtraction (-):

sub = num1 - num2  # sub = 15 - 4
                   #     => 11

print("\nSubtraction: ", sub) # o/p: 11

# 3. Multiplication (*):

mul = num1 * num2  # mul = 15 * 4
                   #     => 60

print("\nMultiplication: ", mul) # o/p: 60

# 4. division (/):

div = num1 / num2                        # 4 ) 15 (3.75 <-- this is the division answer
                                         #     12
                                         #     ---
                                         #      300 
                                         #      300
                                         #      ----
                                         #        0

print("\nDivision: ", div) # o/p: 3.75

# 5. Floor division (//): -> Return closerst 'integer' which is lesser than or equal to the float value(result of the division)

floor_div = num1 // num2                  # 4 ) 15 ( 3.75 <-- this is the division answer
                                           #     12        -> this division answer convert the closerst integer (3) which is the less than division result(3.75)
                                           #     ---         
                                           #       300
                                           #       300
                                           #      ----
                                           #        0

print("\nFloat division: ", floor_div)  # o/p: 3

# 6. Modulo or remainder (%): -> Return remainder of the division

mod = num1 % num2                  # 4 ) 15 ( 3 
                                   #     12        
                                   #     ---         
                                   #       3 <-- this is the modulo or remainder answer
print("\nModulo: ", mod) # o/p: 3

# 7. Exponentiation (**):

power = num1 ** num2        #  15^4 = 50625

print("\nExponentiation: ", power) # o/p: 50625