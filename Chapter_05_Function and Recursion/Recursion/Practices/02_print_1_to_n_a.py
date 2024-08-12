# WARP to print 1 to n (print by backwards)

def display(n):    # Recursive function
    if (n==0):
        return
    else:
        display(n-1)
        print(n)

display(4)    # calling function


'''
                                Explain
            
    
                 -------------------------------------
                                       
                       display(0)         control return display(1)             
                                  
                 -------------------------------------
                                    1st o/p:  
                       display(1)          1                    -> display(1) call display(0)
                                   
                 -------------------------------------
                                    2nd o/p:
                       display(2)          1                     -> display(2) call display(2)   
                                           2
                 -------------------------------------
                                    3th o/p:
                       display(3)           1                    -> display(3) call display(2)
                                            2
                                            3
                --------------------------------------
                                    4th o/p:
                       display(4)           1                    -> display(4) call display(3)       
                                            2
                                            3
                                            4
                --------------------------------------
                backward direction to provide output

'''