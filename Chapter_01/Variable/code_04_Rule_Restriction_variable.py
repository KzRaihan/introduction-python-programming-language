'''
    -> Variable(Identifier) are like a container to storing data.

        >> Rule_01
            A variable name can only contain alpha-numeria characters and underscores.
            
        
        >> Rule_02
           1st character is alphabet (letter) or Underscore(_) || can't start with a number or digit(0-9)
            
            
        >> Rule_03
            can't use special symbol || no comma  || No blank space  
        
        >> Rule_04
            Variable are case sensitive 
        
        >> Rule_05
           Identifier can be of any length. 
        
        >> Rule_06
           Identifier name can't be  same of data type name.
            

'''
print("Rule and Restriction of variable in Python")

print("Valid Variable in python")
# valid variable declaration and assign the value
var_1 = 6
Var_1 = 725
name = "KzRaihan"
number = 100
price = 290.99

print("var_1:", var_1) # case sensitive
print("Var_1: ", Var_1)
print("Name: ", name)
print("Number is : ", number)
print("Book prices: ", price)

#valid variable
Fix_price = 1000
pi = 3.1416
_1var = 99
myAge = 23
MyFullName = "MD Kamruzzaman Raihan"

print("Fix price: ",Fix_price)
print("pi value : ",pi)
print("_1var    : ",_1var)
print("myAge    : ",myAge)
print("MyFullName:",MyFullName)

#invalid variable declaration and assign the value
'''
    10_var = 90
    1variable = 800
    var! = "invalid"
    #var = 456
    fix,price = 99.99
    my Name = "ooo"
    int = 4
    float = 5.00 
    double = 6.00004
    char = 'a'

'''



