# eg_01: basic print

print("\nExample one\n")

i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

"""   
       code explain
    ==================

    1st iteration
    ---------------
-> init: i = 1

-> while cds: i <= 5
             = 1 <= 5 (T)
    
    --> if_cds: i == 3
             => 1 == 3 (F)
-> body:
       print: i                                 o/p: 1
            = 1
-> inc: i = i + 1
          = 1 + 1
          = 2
   
    2nd iteration
    ---------------

-> while cds: i <= 5
            = 2 <= 5 (T)
    
    --> if_cds: i == 3
             => 2 == 3 (F)
-> body:
       print: i                                 o/p: 1
            = 2                                      2
-> inc: i = i + 1
          = 2 + 1
          = 3
             
    3th iteration
    ---------------

-> while cds: i <= 5
            = 3 <= 5 (T)
    
    --> if_cds: i == 3
             => 3 == 3 (F)
        
        ---> inc: i = i + 1
                    = 3 + 1
                    = 4
        ---> continue
              >> below the continue statement is not execute
     
     4th iteration
    ---------------

-> while cds: i <= 5
            = 4 <= 5 (T)
    
    --> if_cds: i == 3
             => 4 == 3 (F)
-> body:
       print: i                                 o/p: 1
            = 4                                      2
-> inc: i = i + 1                                    4
          = 4 + 1
     
     5th iteration
    ---------------

-> while cds: i <= 5
            = 5 <= 5 (T)
    
    --> if_cds: i == 3
             => 5 == 3 (F)
-> body:
       print: i                                 o/p: 1
            = 5                                      2
-> inc: i = i + 1                                    4
          = 5 + 1                                    5
          = 6
             
     6th iteration
    ---------------

-> while cds: i <= 5
            = 6 <= 5 (F)
-> end of loop
    
>> so, final o/p:
                 1
                 2
                 4
                 5
    
"""