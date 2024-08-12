'''   
Topic: Recursion Function

-> Recursion is a method where a function calls itself. 
     --> It solves a problem by breaking it down into smaller subproblems of the same type.

-> Three part:
     --> Function Definition: Function is start here
     --> Base Case(Stop cds) : Function is stop 
     --> Work: 
            Recursive Case : Function calls itself
            Other case  

'''
# Print n to 1 (backwords)
def show(n):           # <-- this is function definition part or recursion function

     if(n == 0):       # <-- this is base case or cds
          return
     print(n)     # <- this are work
     show(n-1)    #
     
     print("End") # this is other work

show(4)   # calling function


'''   
                      Explain Code

when n = 4
----------------------

def show(4):
     if(4==0) -> False

     print(4)                       o/p:  4
     show(3) or show(4-1)
    
    now, control go to show(3) function
    
when n = 3
----------------------

def show(3):
     if(3==0) -> False

     print(3)                       o/p:  4 
                                          3
     show(2) or show(3-1)
    
    now, control go to show(2) function
    
when n = 2
--------------------

def show(2):
     if(2==0) -> False

     print(2)                       o/p:  4 
                                          3
                                          2
     show(1) or show(2-1)
    
    now, control go to show(1) function
    
when n = 1
--------------------

def show(1):
     if(1==0) -> False

     print(1)                       o/p:  4 
                                          3
                                          2
                                          1

     show(0) or show(1-1)
    
    now, control go to show(0) function
    
    
when n = 0
------------------
def show(n):
     if(0==0): -> True
          return           -> this return means control show(1)
                           


    
    now, control go to show(1) function


    now, backword:


def show(1):
     if(1==0) -> False

     print(1)                       o/p:  4 
                                          3
                                          2
                                          1

     show(0) or show(1-1)
     print("End")                   o/p:  End
    
    now, control go to show(2) function 
    


def show(2):
     if(1==0) -> False

     print(1)                       o/p:  4 
                                          3
                                          2
                                          1

     show(1) or show(2-1)
     print("End")                   o/p:  End
                                          End
    
    now, control go to show(3) function 
    
    def show(3):
     if(3==0) -> False

     print(3)                       o/p:  4 
                                          3
                                          2
                                          1
     show(2) or show(3-1)           o/p:  End
                                          End
                                          End
    
    now, control go to show(4) function
                  and
     when, we call show(4) then it will provide output:
        output:
                4
                3
                2
                1
                End
                End
                End


'''



