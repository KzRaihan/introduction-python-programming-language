""" 
 Topic: list in python
 obj: A built in data type that stores set of values
     
     - It can store element of different types [integer, float, string, etc]
     - list are mutable(changeable of values)

 Syntax:
     list_name[value1, value2, ......]
     
     -> list_name is similar to variable name
"""
# eg_01: same values
marks = [97.07, 88.89, 95.45, 96.39, 99.99]
print(marks)
print("Type of marks: ", type(marks))
print("length of marks: ", len(marks))

# eg_02 : different values
student_details = ["Kz", 23, "CSE", 96.5]
print("\nStudent Details: ", student_details)
print("Type: ", type(student_details))
print("length: ", len(student_details))

