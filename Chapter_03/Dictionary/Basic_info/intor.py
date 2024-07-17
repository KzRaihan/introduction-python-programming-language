""" 
Topic : Dictionary

obj  : A dictionary is a collection of key-value pairs.
  - Keys must be unique (immutable) or duplicate keys don't allow(support).
  - Values can be of any type.

syntax:
    dic_name = {
      key1: value1,
      key2: value2,
         ...
     keyN: valueN
    }
"""
# Create a dictionary
dic_name = {
    "key" : "Value",
    "name": "Kz", 
    "age" : 23, 
    "city": "Dhaka",
    "is_student": True,
    "grade": 95.5
}
# access dic_name
print("Dictionary: ", dic_name)
print("Type : ", type(dic_name))

# dic are unordered, mutable(changeable) and don't allow duplicate keys.
""" 
Dictionary values:
-------------------

Can be of any type, including:
  - Integers (int)
  - Floats (float)
  - Strings (str)
  - Booleans (bool)
  - Tuples (tuple)
  - Lists (list)
  - Dictionaries (dict)
Other objects, such as user-defined classes

Dictionary keys:
-----------------

Must be immutable and hashable, which means:
  - Strings (str) are allowed as keys
  - Integers (int) are allowed as keys
  - Tuples (tuple) are allowed as keys, but only if they contain immutable elements
  - Lists (list) are not allowed as keys, because they are mutable
  - Dictionaries (dict) are not allowed as keys, because they are mutable
Other objects, such as user-defined classes, can be used as keys if they are immutable and hashable
"""