""" 
Topic : dictionary
obj  : add new pairs(key and value)
"""
dic_add ={
    "Name": "Kz", 
    "Age": 23,
    "Address": {"city ": "Dhaka", "state": "Mirpur"}
}

print("Original Dictionary: ", dic_add)
print("Length: ", len(dic_add))

# Add new pairs
dic_add["Phone"] = "01770428609"

print("\nDictionary after adding new pairs: ", dic_add)
print("Length: ", len(dic_add))

# add another pairs
dic_add["ID"] = 4039

print("\nDictionary after adding another pairs: ", dic_add)

# add last name
dic_add["last Name"] = "Raihan"

print("\nDictionary after adding last name: ", dic_add)
print("Length: ", len(dic_add))

# key can't be same name
dic_add["Name"]= "Md" # change Name key value or overwrite Name key

print("\nDictionary after changing name: ", dic_add)