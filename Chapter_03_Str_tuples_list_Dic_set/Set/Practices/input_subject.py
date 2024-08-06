"""  
WAP to enter mark of 3 subjects from the user and store them in a dictionary.
start with an empty dictionary and add one ny one. use  subject name of key and marks as value
"""
# create an dic
dic ={}

# ask user to input marks for 3 subjects
sub1 = input("Enter Your First subject name: ")
sub2 = input("Enter your second subject name: ")
sub3 = input("Enter your Third subject name: ")

# add marks to the dictionary
dic[sub1] = 80.56
dic[sub2] = 90.36
dic[sub3] = 98.0

# print the dictionary

print("Dictionary: ", dic)