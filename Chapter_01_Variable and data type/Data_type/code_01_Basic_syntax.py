'''
             Data type
        -----------------
    -> Definition:
         Data type defines the what kind of values that variable can hold.
    
    -> Type of Data type
       1. Numeric Data type
           --> int (Represent whole numbers)
           --> float(decimal numbers)
       2. Text type
          --> str (string type or sequence of characters)
       3. Boolean type
          --> bool (either true or false)
       4. None type
          --> the absence of a value

'''
print("\n1. Numeric Types ")
print("-----------------------")

print("Integer(int) Data type\n")
num1 = 100  # not accept floating value
num2 = -20
num3 = 500

print("num1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)
print("Data type: ", type(num1))

print("\n\n2.floating(float) Data type\n")
num1 = 100.00  # accept floating value
num2 = -20.92
num3 = 500.36

print("num1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)
print("Data type: ", type(num1))

print("\n\n3. Text Types ")
print("-----------------------")

print("String(str) Data type\n")
name = "KzRaihan"
Book_name = "python programming language"
country = "Bangladesh"

print("name = ", name)
print("Book_name = ", Book_name)
print("country = ", country)
print("Data type: ", type(name))

print("\n\n4. Boolean Types ")
print("-----------------------")

print("Bool(bool) Data type\n")
age = True
old = False

print("age = ", age)
print("old = ", old)
print("Data type: ", type(age))

print("\n\n5.None(none) Data type ")
print("-----------------------")

Not_define = None

print("Not_define = ", Not_define)
print("Data type: ", type(Not_define))