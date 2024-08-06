""" 
Topic: dictionary 
obj  : generate error
    -> if that key is access which is not within dic then it can generator error message 
"""
dic_error ={
    "Name" : "Kz",
    "university": "SU", 
    "Subject " : ["Python", "C", "Java"],
    "mark": (96.66, 92.5, 90.00),

}
# access key pairs(key and value)
print("Dic: ",dic_error)   # o/p all key pairs
print("Type: ", type(dic_error)) # o/p type: dic
print("Length: ",len(dic_error)) # Length: 4(total number of key or key pairs)

# Generated error : when we access key which is not present in our dic_error dictionary
print(dic_error["First name"]) # KeyError -> because First name key is not our dic

# Solution: check if key is present in our dictionary or not

if "First name" in dic_error:
    print("Key 'First name' is present in our dictionary.")
else:
    print("Key 'First name' is not present in our dictionary.")
