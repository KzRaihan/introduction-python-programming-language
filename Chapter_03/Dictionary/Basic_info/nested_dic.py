""" 
Topic: Nested dictionary
obj  : A dic contains another dic as it's value

Syntax:
   outer_dic={
    "key1" : "val1"
    --------------
    inner_dic:{
         here, inner dic keys pairs
         "inner_key" : "inner_values",
    } end of inner dic

   } end of outer dic
"""
# eg_01
outer_dic={
    "Name": "Kz_Raihan",
    "age" : 23,
    "inner_dic":{
        "country" : "Bangladesh", 
        "city" : "Dhaka",
        "hobbies": ["Coding", "Writing","Playing"], 
        "ports" : ("football","basketball")
    }
}
# print whole or entire dic
print("ENTIRE DIC: ", outer_dic)

# print only inner dic
print("\nInner dic: ", outer_dic["inner_dic"])

# print individual key pair in outer dic
print("\nName: ", outer_dic["Name"])
print("age: ", outer_dic["age"])

# individual key pair inner dic
print("\nhobbies: ", outer_dic["inner_dic"]["hobbies"])
print("Country: ", outer_dic["inner_dic"]["country"])

# to modify the value of inner dic
outer_dic["inner_dic"]["city"] = "Mymensingh"

# print after modification
print("\nAfter modification: ", outer_dic)

# to add new key-value pair in inner dic
outer_dic["inner_dic"]["message"] = "Do somethings"
print("\nNow dic: ", outer_dic) 
