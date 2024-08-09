# >> 1. Definition : Dictionary is a collection of keyvalue pairs.

# >> 2. Properties: 
#         -> It is used to store data values in key:value paris
#         -> It is unordered, mutable(changeable of value)
#         -> It don't allow duplicate keys

# >> 3. Syntax:
#       dic_name ={
#              "key" : "values",                    -> key can be string, integer, float, tuples || can't list, dic
#              ............... ,                    -> values can be anything(accept all data type values)
#              ................,
# }

# >> 4. Example of dic

dic = {
    "Key" : "values",
    "name": "KzRaihan",     # key -> str and values -> anything
    "age": 23,
    "is_adult": True,
     
     6 : "Favorite",       # key -> int, float and values = anything
     10.20: 99.99

}

# access of dic paris
print(dic)
print("Type: ", type(dic))

# Mutable
dic[10.20] = 100

print(dic)

# duplicate keys are not allowed
dic["name"] = "Kz"      # it can update the value of name 
print(dic)