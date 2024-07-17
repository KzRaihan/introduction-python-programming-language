"""   
Topic: dic.get("key") method
obj  : return the value according to key
       -> single value return 
"""
dic = {
    "name": "Rahim",
    "age": 23,
    "city": "Dhaka"
}

# get the value of "age" key (this is useful compare to direct access)

value = dic.get("age")
print(value)  # Output: 23
print(dic.get("city"))

# direct access
print(dic["age"])