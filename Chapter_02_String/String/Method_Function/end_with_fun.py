""" 
  Topics: String endswith()
# Return true if string ends with substring
# str.endswith("an") that mean str string end with an or not if yes then o/p: true else o/p: false

Syntax:
     string_name.endswith("Require message")
"""

name = "My name is KzRaihan"

print(name.endswith("an"))  # o/p: True
print(name.endswith("n"))   # o/p: True


print(name.endswith("R")) # o/p: False
print(name.endswith("a")) # o/p: False

# using if condition for endswith function()

if(name.endswith("n")):
    print("Given Name is valid")
    print("name : ", name)
else:
    print("This name is not valid")





