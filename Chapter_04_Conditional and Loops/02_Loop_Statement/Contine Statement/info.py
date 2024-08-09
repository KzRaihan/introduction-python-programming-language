"""  
Topic: continue statement

obj  : Skip the particular set of line then we use continue statement.
     

"""
# eg_01: basic print
print("\nExample one: ")
i = 1
while i <= 5:
    if(i == 3):
        continue  # continue means we skip the below codes or statements
    print(i)
    i += 1

print("Hello Everyone")



"""  
     code explain
     =================

     1st iteration
     --------------
-> ini: i = 1

-> while cds: i <= 5
            = 1 <= 5(T)
          
    --> if cds: i == 3
             => 1 == 3(F)
             
        ->> body: 
                print : i                     o/p: 1
                      : 1

-> inc: i = i + 1
               = 1 + 1
               = 2

     2nd iteration
     --------------
-> i = 2

-> while cds: i <= 5
            = 2 <= 5 (T)
          
    --> if cds: i == 3
             => 2 == 3(F)
                                              
        ->> body: 
                print : i                           o/p: 1
                      : 2                                2

-> inc: i = i + 1
               = 1 + 1
               = 2
     3th iteration
     --------------
-> i = 3

-> while cds: i <= 5
            = 3 <= 5 (T)
          
    --> if cds: i == 3
             => 3 == 3(T)
                continue
                >> for this continue statement below the code is not execute or skip the below all code.
                >> Hello Everyone statement(code) is not execute.

so, final output: 
                 1
                 2

"""