""" topic: dic.update(new_dic)
 obj : inserts the specified items to the dictionary
     -> concatenation or two or more dic in one dic
     -> this method return None 
 syntax: 
     dic_name.update(new_dic)
    
 for single paris
     dic_name.update({"key": value})
 for multiple key paris
     dic_name.update({"key": value, "Key": value,....."KeyN":ValueN},)
"""
my_dic={
    "name": "kz",
    "age": 30
}

new_dic={
    "city": "Dhaka",
    "job": "Software Engineer"
}
# print my_dic 
print("My dic value: ",my_dic)

# new_dic 
print("New dic value: ",new_dic)

# update my_dic with new_dic
print("My_dic + new_dic: ", my_dic.update(new_dic)) # in the store of -> my_dic = my_dic + new_dic 
print("my_dic: ", my_dic)

# eg_02: update single key pairs
my_dic.update({"ID": 4039}) # my_dic ={...previous pairs..., 'ID': 4039}
print("my_dic: ", my_dic)

# eg_03 : multiple pairs update
new_dic.update({"Job Title": "Ml engineer", "Job Location":"Finland"})
print("\nAfter UPDATE: ", new_dic)

# overwrite key value when update using same key
my_dic.update({"name": "Kz_Raihan"})
print("\nRename",my_dic)

# final update
my_dic.update(new_dic)
print("\nFinal update: ", my_dic)

 
