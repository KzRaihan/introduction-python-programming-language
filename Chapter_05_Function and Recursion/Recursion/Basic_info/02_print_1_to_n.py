# print 1 to n using recursion function
def display(num,star_num = 1):  # Recursion function
    if(star_num == num+1):
        return
    else:
        print(star_num)
        display(num, star_num + 1)


num = int(input("Enter Your End number: "))
display(num)  # calling function


'''
                       code explain
    when,
        num = 4 , start_num = 1
    -----------------------------------------
    
    def display(4,start_num = 1):     # star_num = 1 -> this is default parameter
        if(start_num == 4+1):         # 4+1 = 5 -> if condition is false, recursion can't stop 
         => 1 == 5 (False)
            return
        else:
            print(start_num)           # print 1
            display(4, start_num + 1)  # call function again with start_num = 2 (1+1)
    when,
        num = 4 , start_num = 2
    ------------------------------------------
    
    def display(4,start_num = 2):     # star_num = 1 -> this is default parameter
        if(start_num == 4+1):         # 4+1 = 5 -> if condition is false, recursion can't stop  
          => 2 == 5(False)
            return
        else:
            print(start_num)          # print 1
                                              2
            display(4, start_num + 1)  # call function again with start_num = 3 (2+1)
    when,
        num = 4 , start_num = 3
    ------------------------------------------
    
    def display(4,start_num = 3):     # star_num = 1 -> this is default parameter
        if(start_num == 4+1):         # 4+1 = 5 -> if condition is false, recursion can't stop 
          => 3 == 5(False)
            return
        else:
            print(start_num)          # print 1
                                              2
                                              3
            display(4, start_num + 1)  # call function again with start_num = 3 (3+1)
    when,
        num = 4 , start_num = 4
    ------------------------------------------
    
    def display(4,start_num = 4):     # star_num = 1 -> this is default parameter
        if(start_num == 4+1):         # 4+1 = 5  -> if condition is false, recursion can't stop 
          => 4 == 5(False)
            return
        else:
            print(start_num)          # print 1
                                              2
                                              3
                                              4
            display(4, start_num + 1)  # call function again with start_num = 5 (4+1)
    when,
        num = 4 , start_num = 5
    ------------------------------------------
    
    def display(4,start_num = 5):     # star_num = 1 -> this is default parameter
        if(start_num == 4+1):         # 4+1 = 5  -> if condition is true, recursion stops  
          => 5 == 5(True)
            return
    
    now, return the control top to bottom
                 
                    display(4,5) 
                    display(4,4) 
                    display(4,3) 
                    display(4,2) 
                    display(4,1) 

   when we will call display(4, 1) then provide output:
                                      1
                                      2
                                      3
                                      4
                                      5


'''