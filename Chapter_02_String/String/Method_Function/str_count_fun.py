""" 
Topics: str.count("message")

key point: counts the occurence of substring(word)
"""
str1 = "There are many many people live in BD"

# count the occurrence of 'many'
count_many = str1.count("many")

print("str1 : ", str1)
print("Number of many in str1: ", count_many)

# wap to input a string form user and then if k is exist 2 times then print original message
user_input = input("Enter any message: ")

k = user_input.count("k")

if k == 2:
    print("True")
    print("Original Message: ", user_input)