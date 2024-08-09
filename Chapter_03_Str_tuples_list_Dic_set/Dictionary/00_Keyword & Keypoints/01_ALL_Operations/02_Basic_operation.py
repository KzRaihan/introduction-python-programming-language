# Basic operation of dictionary

# 1. same or general key pairs 
print("\n1. same key type: ")


    # General dictionary when key -> str . and value = anything

dic_1 = {
    "name": "KzRaihan",
    "age": 30,
    "city": "Finland"
}

print(dic_1)   


# 2. when key -> different data type and value = anything
print("\n2. Different key type: ")

dic_2 = {
     "str_key" : "Finland",     # key -> string
     10 : "integer key",        # key -> int
     99.99 : 2024,              # key -> float
     True : True,               # key -> Boolean
     (1,2,3) : (10, 20, 30, 40)    # key -> tuples

}

print(dic_2)

# 3. individual key vales access by using index as key
print("\n3. Individual key values access by using index as key")

print(dic_2["str_key"])
print(dic_2[10])
print(dic_2[99.99])
print(dic_2[True])
print(dic_2[(1,2,3)])

# 4. Generate error : when key is not within dictionary
# print(dic_2["First_name"])

# 5. Create an Empty dictionary
print("\n5. Create an empty dic and add key pairs, new dictionary")

# Empty dictionary
null_dic = {}

# add key pairs
print("\nAdd some key pairs")

null_dic["Name"] = "Raihan"
null_dic["city"] = "Finland"

print(null_dic)

# add new dict 
new_dic = {
    "Study": "Python",
    "interest" : "Ml and Deep learning"
}

null_dic["new_dic"] = new_dic      # -> this also called nested dictionary 
print("\nafter adding then dic: ", null_dic)


# 6. Nested dic
main_dic = {
    "Name" : "KzRaihan",
    "age" : 30,
    "ID"  : 4039,

    "Nested_dic":
    {
        "Math" : 90,
        "Physic" : 92,
        "ICT" : 98.05
    }
}

print("\n6. Access Main & Nested dic: ", main_dic)

print("\nAccess nested dic: ", main_dic["Nested_dic"])

print("\nAccess nested dic value : ", main_dic["Nested_dic"]["ICT"])


