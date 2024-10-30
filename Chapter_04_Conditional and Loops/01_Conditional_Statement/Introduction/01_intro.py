"""
 >> Definition: Used to execute a code block if a condition holds true.
 >> Type of condition statement
    -> if statement
    -> if-else statement 
    -> elif statement
    -> nested if-else statement

>> Syntax of condition statement:
   -> if condition statement
      if(condition):
          ----------
          ----------          this is the body of if statement
          statements
          ----------
          ----------
      else:
          ----------
          ----------          this is the body of else statement
          statements
          ----------
          ---------
   -> elif statement condition statement
      if(condition):
          ----------
          ----------          this is the body of if statement
          statements
          ----------
          ----------
      elif(condition):
          ----------
          ----------          this is the body of elif statement
          statements
          ----------
          ----------
      else:
         ----------
         ----------          this is the body of else statement
         statements
         ----------
         ---------
    

"""
# if statement with single condition
# eg_01 for single value
num1 = 10
if(num1):
    print("True Number")      # this is the o/p.
else:
    print("False Number")

# eg_02

num2 = 0
if(num2):
    print("True Number")     
else:
    print("False Number")    # this is the o/p.

#eg_03: for comparison value cds
age = 20

if(age >= 18):
    print("Adult")
    print("They can vote")
    print("They can Drive")
else:
    print("Not Adult")
    print("They can't vote")
    print("They can't Drive")
