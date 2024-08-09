"""
 >> Accessing part of a string or substring

   -> Syntax:
         string name[starting idx: ending idx] # ending idx is not include

"""
# eg_01
str1 = "Kamruzzaman Raihan"   

# accessing substring form 0 to 11 but 11 idx is not include
sub1 = str1[0:11] 
print("Substring_1: ", sub1)
print("length: ", len(sub1))


# eg_02
sub2 = str1[12:len(str1)] # sub2 = str1[11:18]
print("Substring_2:", sub2)
print("length: ", len(sub2))

# eg_03(when first index is not declare then it is automatic assign similar for last idx)
print("Substring_03:",str1[:8])
print("Substring_04:",str1[5:])
# print("Substring_000:",str1[5:1]) this provides not output because accessing order in smaller to upper


# eg_04 : negative indexing is allow only slicing in python
str2 = "Bangla"    #  for +ve idx: increase index(0,1......so on)

# str2[-1] = a        for -ve idx: decreases index(-1,-2......so on) using when we can't known the length of string.
# str2[-2] = l    
# str2[-3] = g
# str2[-4] = n
# str2[-5] = a
# str2[-6] = B

print("Negative substring_01:", str2[-4:-1])   # accessing order in smaller to upper
print("Negative substring_01:", str2[-6:-3])   # can't in accessing str2[-3:-6] this order
print("Negative 0215:", str2[-3:-6])           # there is no output


