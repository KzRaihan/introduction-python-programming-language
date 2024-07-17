""" 
Topic: dic.keys()
obj  : to return all keys in dictionary
-> format: target_data type(source data type)
"""
my_dic={
    "name": "Kz_Raihan",
    "age": 23,
    "city": "Dhaka",
    "is_student": True    
}

# print all keys
print(my_dic.keys())

# keys convert dic to list -> Direct conversion that not impact to main dic

print(list(my_dic.keys())) # target_data type : list and source data type : my_dic
print("Type: ", type(my_dic)) # Type: dic

# other way -> first create list(list_dic) then convert my_dic to list and store list_dic
list_dic = list(my_dic) # my_dic is store into list_dic
print(list_dic)
print("Type: ", type(list_dic)) # Type : list