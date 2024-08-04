"""  
Topic: Function type 

>> there are two type of function
 -> 1. Built in function(standard library function)
 -> 2. user define function(UDF)

 >> 1. Built in function:
       -> print()
       -> len()
       -> type()
       -> range()
          etc 
 
 -> syntax: the syntax of print built in function
    

     function_name(arguments)
        -> sep : " "
        -> end : "\n"

    print(value, sep:" ", end: "\n")
    
eg_01:
    print("Hello", "I am Kz_Raihan")

-> here, 
   print = function name
   arguments =  Hello and I am Kz_Raihan
   
"""



#eg_01: code part

print("Hello")
print("I am KzRaihan")




"""  
    code explain:
 output: 
    > Hello 
    > I am KzRaihan
    
    -> before Hello always print new line 
    -> before I am KzRaihan always print a new line 

   in print() syntax say that after end the statement print a new line
"""
# if you not need to new line -> how to solve

# 1st way to solve  
print("\nsolution first way: ")
print("Hello", "I am KzRaihan")

# 2nd way to solve
print("\nsolution second way: ")

print("Hello", end = " ")  # end = " " means when end the statement print space(not new line)
print("I am KzRaihan")

# in print() syntax say that after comma the statement print a space 

print("\nUpdate the space")

print("Kz", "Raihan")  # o/p: Kz Raihan (but we do not need the space between two statement)
# to solve this problem
print("\nSolution the space problem: ")
print("Kz","Raihan", sep = "") 

# sep = "&" this will print the & sign between two statements
