""" 
   -> concatenation: To add two or multiple string
   -> length of string: how many character is present in string.
      syntax: 
            len(string_name)  .here len() is function
      count capacity:
         >> Space or white string
         >> special character
         >> character
         >> integer(all digit)
         >> Escape sequence(always count 1)

"""
# Concatenation
first_name = "Kz"
last_name = "Raihan"

full_name = first_name + "_" + last_name  # here three str is add
print("Full name: ", full_name)

# Length of string
len1 = len(first_name)
len2 = len(last_name)

print("length of first_name: ", len1) # 2
print("length of last_name: ", len2)  # 6

print("Length of Full name: ", len(full_name)) # 2 + 1 + 6 = 9

# for escape sequence(count 1)
str0 = "Kz\nRaihan"
len_str0 = len(str0)
print("Length of str0: ", len_str0) # 9 -> 2 + 1 + 6 

