""" 
Topic: dic.values() method
obj  : return all values in dictionary
>> dic means dictionary name
"""
# eg_01:
dic = {
    "name" : "KzRaihan", 
    "age" : 25,
    "city": "Dhaka",
    "is_student": True,
    "grade": 95.5,
    "marks": {
        "c": 85,
        "C++": 90,
        "java": 92,
        "Python": 98,
    }
}
# print all values
print("\nValues of all keys: ", dic.values())
# convert dic to list
print("\ndic to list", list(dic.values()))
# other way to convert dic to list
list1 = list(dic.values())
print("\nAnother way o/p: ", list1)
