"""  
Topic: while loop
obj  :  cds type (cds comparison values)
     -> two value are need 

"""
# eg_01: 
i = 1
count = 1
while i <= 10:
    print("Iteration: ", count)
    print("Value:", i)
    i += 2
    count += 1

# eg_02:
print("\nExample two\n")
count = 10
while count >= 1:
    print(count)
    count -= 1

# eg_03: print form 1 to 50 
print("\nExample three: \n")
i = 1

while i <=  50:
    print(i)
    i += 1

"""  
      code explain
 when we perform comparison type of value in loop we will focus on
      -> star point
      -> end point
      -> increment/decrement size

>> explain eg_01:
 here, 
    start = 1
    end   = 10
    inc by = 2
  
          1st iteration
    -> init: i = 1

    -> cds: i <= 10
          = 1 <= 10 (True)

        -> L_body:
             print: iteration : count
                   = iteration: 1                o/p: iteration: 1
                                                      value : 1
             print: value : i           
                   = value: 1
    
    -> increment: i += 2
                => i = i + 2
                     = 1 + 2
                     = 3 
    
    -> increment: count = count + 1
                        = 1 + 1
                        = 2
          2nd iteration
    -> init: i = 3
         count = 2

    -> cds: i <= 10
          = 3 <= 10 (True)

        -> L_body:
             print: iteration : count
                   = iteration: 2                o/p: iteration: 2
                                                      value : 3
             print: value : i           
                   = value: 3
    
    -> increment: i += 2
                => i = i + 2
                     = 3 + 2
                     = 5
    
    -> increment: count = count + 1
                        = 1 + 1
                        = 2
          
          3th iteration
          --------------

    -> init: i = 5
         count = 3

    -> cds: i <= 10
          = 5 <= 10 (True)

        -> L_body:
             print: iteration : count
                   = iteration: 3                o/p: iteration: 3
                                                      value : 5
             print: value : i           
                   = value: 5
    
    -> increment: i += 2
                => i = i + 2
                     = 5 + 2
                     = 7
    
    -> increment: count = count + 1
                        = 3 + 1
                        = 4
       
          4th iteration
          --------------

    -> init: i = 7
         count = 4

    -> cds: i <= 10
          = 7 <= 10 (True)

        -> L_body:
             print: iteration : count
                   = iteration: 4                o/p: iteration: 4
                                                      value : 7
             print: value : i           
                   = value: 7
    
    -> increment: i += 2
                => i = i + 2
                     = 7 + 2
                     = 9
    
    -> increment: count = count + 1
                        = 4 + 1
                        = 5
       

          5th iteration
          --------------

    -> init: i = 9
         count = 5

    -> cds: i <= 10
          = 9 <= 10 (True)

        -> L_body:
             print: iteration : count
                   = iteration: 5                o/p: iteration: 5
                                                      value : 9
             print: value : i           
                   = value: 9
    
    -> increment: i += 2
                => i = i + 2
                     = 9 + 2
                     = 11
    
    -> increment: count = count + 1
                        = 5 + 1
                        = 6
       
          5th iteration
          --------------

    -> init: i = 11
         count = 6

    -> cds: i <= 10
          = 11 <= 10 (False)

    -> out of loop body

    >> final o/p:
          iteration: 1
          value    : 1
          
          iteration: 2
          value    : 3
          
          iteration: 3
          value    : 5

          iteration: 4
          value    : 7

          iteration: 5
          value    : 9
       

"""