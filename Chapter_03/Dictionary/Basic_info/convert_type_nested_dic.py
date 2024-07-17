# Topic: Nested dictionary 
# obj  : To convert dic to list or list to tuple

# eg_01
student = {
    "name" : "Kz_Raihan", 
    "Id"   : 4039,
    "marks" : {
        "math" : 80,
        "english" : 90,
        "science" : 85
    }
}
# access whole dic
print("Original dic: ", student)
print("Type: ", type(student))

# convert dic to list
print("Convert dic to list: ", list(student))
