"""
Topic: indexing of string
-------------------------
 String is a character type of array

 Array means : Data element arranged in sequentially manner(each element is connected to it's previous and next element).
 
 Indexing :
 index help to accessing character but can't modify
    >> index start with: zero
    >> index end with  : length of string - 1
"""

str1 = "Kz_Raihan"    
# str1[0] = K
# str1[1] = z
# str1[2] = _
# str1[3] = R
# str1[4] = a
# str1[5] = i
# str1[6] = h
# str1[7] = a
# str1[8] = n

# accessing element of string(single element)
ch1 = str1[0]
ch2 = str1[8]

print("Character at index 0 :", ch1)
print("character of index 8: ", ch2)

# str1[3] = m -> it's not allow in python
