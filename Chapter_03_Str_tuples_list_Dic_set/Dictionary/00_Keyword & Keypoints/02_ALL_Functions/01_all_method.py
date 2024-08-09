# Dictionary method

# 1. dic.key() : -> Return all key in dic

dic = {
    "Name": "Raihan",
    "age" : 23,
    "country": "Finland"
}

# 1. dic.items() : -> Return all key paris(key: value) as tuple form
print("\n1. Print all key pairs in dic: \n", dic.items())

# convert tuple to list form
print("\nconvert tuple to list: ", list(dic.items()))

# another way to access key pair
all_paris = dic.items()
print("\nAll key pairs : \n", all_paris)
print("\nType: ",type(all_paris))  # < dic > 

# # 2. dic.keys() -> Return all keys name

print("\n2. Print all dictionary key:\n",dic.keys())

# 3. dic.values() : -> Return all values in dic
print("\n3. Print all values in dic: \n", dic.values())

# another way
all_values = dic.values()
print("\nAll values: ", all_values)
print("Type: ", type(all_values))  # < dic_values >


# 4. dic.get(key) : -> Return value(individual) for given key. If key not found, return None

value = dic.get("age")
print("\n4. Get value of 'age' key: ", value)
print("Type: ", type(value))   # < int >

# another way
print("\nGet value of 'Name' key: ", dic.get("Name"))

# Q.n : What is the different between dic["key"] and dic.get("key")

#             dic["key"]                                                   dic.get("key")  
# -> dic["key"] is not function                              ||  ->  dic.get("key") is a function
# -> if, key is not present in dic it return error message   ||  -> if key is not within the dic then it return none, but can't provide error message
#     eg:     
#           before code
#           dic["Last_name"]                                  ||          if last_name is not within dic so interpreter provide none  
#           after code                                                     and execute the after code.
#              
#          last_name is not within dic so interpreter
#          provide error message and can't execute after code         

# 5. dic.copy() -> Returns a shallow copy of the dic.
new_dic = dic.copy()
print("\n5.Copy dictionary: \n", new_dic)

# 6. dic.update(new dic) -> insert the specified items to the dictionary
# first way:
print("insert two key pairs", dic.update({"Study": "CSE", "Learn": "Python"}), dic)

# second way:

new_dic_2 = {"Job Title": "ML engineer", "Job Location":"Finland"}
dic.update(new_dic_2)
print("\n6.Update dictionary with new_dic_2: \n", dic)

# 7. dic.pop(key) -> Removes the item with the specified key from the dictionary
# First way
dic.pop("age")

print("\n7. Remove 'age' key: \n", dic)

# dic.pop("values")      # this values key is not within dic that way, it will provide error 
# print("\n pop 'value' in dic", dic)

# second way
pop_study = dic.pop("Study")
print("\nPop Value: ",pop_study)     # Return the corresponding pop key value || o/p: CSE
print("\nAfter pop 'Study' key:\n", dic)

# 8. dic.popitem() -> Removes the last inserted item (key-value pair) from the dictionary in LIFO order(Last in First out)

dic.popitem()
print("\n8. Remove last inserted key-value pair: \n", dic)

# which item is remove or which item is last pair or last pair is insert
last_pair = dic.popitem()

print("\nLast inserted key-value pair: ", last_pair)

# 9. dic.clear() -> Remove all elements form the dic
dic.clear()
print("\nClear the all key pairs in dic: ",dic)



