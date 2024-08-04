# Operator Precedence:
"""    
      Precedence    |    Operators
        
         1          |     () 

         2          |     *, /, %                # when same precedence then follow associativity Rule
                                                                                     -> Solve left(top Priority) to Right
         3          |      +, - 

         4          |       =     
"""

# eg_01

x = 4 + 9 * 10
print(x)  # o/p: 94

# x = 4 + 9 * 10        1st priority  : *
#   = 4 + 90            2nd priority  : +
#   = 94

# eg_02
y = 4 * 3 / 6 * 2
print(y)  # o/p: 4.0

# y = 4 * 3 / 6 * 2      1st priority  : * 
#   = 12 / 6 * 2          2nd priority : /
#   = 2.0 * 2              3rd priority  : *
#   = 4.0

# eg_03
num1, num2 = 2, 3
txt = "Kz"
ans = '2' + num2 * txt

print(ans)  # o/p: 2KzKzKz

# ans = '2' + 3 * 'Kz'       1st priority  : *
#     = '2' + 'KzKzKz'       2nd priority  : +
#     = '2KzKzKz'