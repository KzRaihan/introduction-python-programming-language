""" 
 Topics: str.replace()
 Objective: Replace old occurrences of a substring with the original string.

 replace can be:
          >> single world
          >> multiple world or sentences(substring)
          >> Hold string

 >> syntax: 
      string_name.replace(old_substring, new_substring)
"""
# Example 1: Replace single or first occurrences of a substring with the original string.

str1 = "Dhaka is my old city"
str2 = str1.replace("Dhaka", "Mymensingh")
print("Replace all occurrences: ", str2)

# Example 2: Replace multiple or substring occurrence of a substring with the original string.
book = "Python and c is my favourite programming language"
print(book.replace("c is ","c++ are "))
