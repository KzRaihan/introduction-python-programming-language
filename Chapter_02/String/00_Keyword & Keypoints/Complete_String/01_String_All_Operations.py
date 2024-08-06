# String is a Data type that stores a sequence of characters.

# There way to express 
str1 = 'First way to single quote'
str2 = "Second way to double quote"        # <- this is the most useful
str3 = '''Third way to triple quote'''

print(str1)
print(str2)
print(str3)

# Basic operation 
# 1. Concatenation: Combines two or more strings
print("\nConcatenation: ")
First_name = "Kz"
Last_name = "Raihan"

full_name = "MD: " + First_name + "_" + Last_name

print(full_name)

# 2. Repetition: Repeats string multiple times
print("\nRepetition: ")
str4 = "Rai"
mul = str4 * 3       # Rai * 3
print(mul)           # RaiRaiRai

# 3. Indexing: Access individual(Specific) characters of string
# String is a immutable data type (values can access but can't be change or modify)
# idx start with = 0
# idx end with = len(str)

print("\nIndexing: ")

str5 = "Bangladesh"

first_idx = str5[0]
second_idx = str5[2]
last_idx = str5[9]
# len1 = len(str5)
# last_idx = str5[len1-1]

print("First character : ", first_idx)
print("second character: ", second_idx)
print("Last character  : ", last_idx)

# can't be modify the values like : str5[0] = 'E' (x : not valid)

# 4. Slicing : Access part of a string
# syntax: str_name[start_idx : end_idx]    # -> end_idx value is not include
# cds must be :  start idx < end idx


print("\nSlicing: ")

str6 = "Python Programming"

# Access first 6 characters

first_six = str6[0:6]
print("First 6 characters: ", first_six)  # Python

# Access last 11 (7-18)  characters

last_eleven = str6[7:18]
print("Last 11 characters: ", last_eleven)  # Programming

# 5. Omitting start and stop idx
# By Default
#      -> start idx count : 0
#      -> stop idx count  : len(str)

print("\n5.Omitting start and stop idx: ")


start_omi = str6[:6]  # start idx automatic count : 0
end_omi = str6[7:]    # end idx automatic count   : len(str6)
both_omi = str6[:]

print(start_omi)
print(end_omi)
print(both_omi)

# 6. Negative indices
# negative idx count right(-1) to left

print("\n6.Negative indices: ")

str7 = "Book"

print("First character: ", str7[-4]) # B
print("Last character : ", str7[-1])  # k

sub_str = str7[-4:-1]   # end idx is not include
print(sub_str)  # Boo

# 7. slicing with skip value
# syntax: 
#     -> str_name[start idx : end_idx : step_size]
#     -> step size : size(gap or skip) between start and end idxs

print("\n7. Slicing with skip value: ")

name2 = "Bangladesh"

skip_two = name2[0:10:2]  # step size : 2   

print(skip_two)  # o/p: Bnlds

skip_three = name2[3:10:3]  # step size : 3
print(skip_three)    # gdh

# revere using negative step size
# for negative step size then count negative idx

rev_name2 = name2[::-1]            # start idx : -1  | end idx : -10  | step size : -1
print("\nReverse name2: ", rev_name2)

rev_last_2d = name2[:-3:-1]        # start idx : -1 (automatically count)
                                   # end idx   : -2 (include)
                                   # step size : -1 (decrement or reverse order) 
print("Last two digit in reverse: ", rev_last_2d)