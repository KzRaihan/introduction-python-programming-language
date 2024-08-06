"""  
Topic : dic.item() method
obj  : return all pairs(key, values) as tuples

-> there are two way to access all pairs
   >> 1. Direct access
   >> 2. using function(which very useful)
"""
my_dic={
    "Name": ["Kz", "Raihan", "Sk", "Rahim"],
    "Age" : (23, 22, 25, 21),
    "City": ["Dhaka", "Chittagong", "Rajshahi", "Sylhet"],
    "Country": "Bangladesh"
}
# print whole dic 1. Direct access
print("\nWhole Key: ", my_dic)

# print using my_dic.item()
print("\nWhole Key: ", my_dic.items())
print("\nType casting Whole Key: ",list(my_dic.items()))