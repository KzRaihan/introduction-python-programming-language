'''
   Type of variable
     -> Two types:
        >> Global Variable
        >> Local variable

'''
print("Global Variable")
print("A global variable is defined outside any function or block of code.")
global_var = 6  # This is a global variable

def my_function():
    print("Global variable inside function:", global_var)

my_function()  # Prints: Global variable inside function: 6

print("Global Variable")
print("A local variable is defined within a function or a specific block of code.")

def my_function():
    local_var = 99  # This is a local variable
    print("Local variable inside function:", local_var)

my_function()  # Prints: Local variable inside function: 99
