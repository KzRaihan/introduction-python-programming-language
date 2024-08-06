""" 
 WAP to count the number of students with the "A" grade in the following tuple
 ("C", "D", "A", "A", "B", "B", "A")

 then store the above value in a list and sort them form "A" to "D".
"""
Grade = ("C","D", "A", "A", "B", "B", "A") # assign tuple
Count_A = Grade.count("A") # count A grade
print("Number of Student with A Grade: ", Count_A )
print("Type: ", type(Grade))

# second part


list = list(Grade) # convert tuple to list(Explicit type conversion Syntax: target data type(source variable name)
list.sort()
print("\nAfter sort in ascending order: ", list)
print("Type: ", type(list))
