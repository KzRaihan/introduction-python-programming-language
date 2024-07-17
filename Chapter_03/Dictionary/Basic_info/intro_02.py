""" 
Topic: Dictionary
obj  : dic can hold different type of value.
"""
# eg_01
dic1 = {
    "Name" : "Kz",           # String type value
    "Age" : 23,              # int type value 

    "list": ["Python", "C", "C++", "Java"], # list type value
    "tuple" : (98, 96.05, 94, 90.50)          # tuple type value
    # here, all key are string
}
print(dic1)
print(type(dic1))

# individual key_value access using key
print(dic1["Name"]) # Kz
print(type(dic1["Name"])) # str

print(dic1["list"])
print(type(dic1["list"]))

print(dic1["tuple"])
print(type(dic1["tuple"]))