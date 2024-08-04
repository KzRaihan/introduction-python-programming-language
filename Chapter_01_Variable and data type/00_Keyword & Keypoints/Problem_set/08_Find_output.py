"""   
 -> Find the output the provide code

      num1 = -23
      num2 = 5

      ans = num1 // num2
      print(ans * 2 + 10)
"""

num1 = -23
num2 = 5

ans = num1 // num2

print(ans * 2 + 10) # o/p: 0

# Explanation:
"""   
   num1 = -23
   num2 = 5

   ans = num1 // num2                              5 ) -23 (-4.6  <- this is the division result 
                                                        20        -> this result convert the closert integer(-5) which is less then division answer(-4.6) 
                                                      ------- 
                                                        -30
                                                         30
                                                        -----
                                                          0
  ans = -5

   ans * 2 + 10
  = -5 * 2 + 10
  = -10  + 10
  = 0

        
"""
