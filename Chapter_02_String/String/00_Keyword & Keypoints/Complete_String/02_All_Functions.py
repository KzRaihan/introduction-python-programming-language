# String Function or method

# 1. str.endswith("last word") : Return True or False

name = "Raihan"
print("End with 'an' or not: ", name.endswith("an"))  # True
print("End with 'ani' or not: ", name.endswith("ani"))  # False

# 2. str.startswith("first word")

print("\nStart with 'Rai' : ", name.startswith('Ra')) # True
print("Start with 'Rah' : ", name.startswith('Rah')) # False

# 3.str.capitalize(): Capitalize only first character in sentence
# it's provide new string
# main string can't change 

sentence = "this is a sentence"
print("\nCapitalize first character: ", sentence.capitalize())  # This is a sentence

# 4. str.title() : Capitalize all first character in sentence
# it's provide new string
# main string can't change 

print("\nCapitalize all first character: ", sentence.title())  # This Is A Sentence

# 5. str.find("word") : Return the idx of the 1st occur

print("\nFind 'is' in sentence: ", sentence.find('is'))  # 2
print(sentence[2])  # i   || this is a sentence

# 6. str.count("world") : counts how many time present is world in a sentence

print("\nCount 'is' in sentence: ", sentence.count('is'))  # 2

# 7. str.replace(old_word, new_word) : Replace old word to new word (if, double then it's also replace)
# it's provide new string
# main string can't change 
print("\nReplace 'is' to 'was' in sentence: ", sentence.replace('is', 'was'))  # thwas was a sentence
print(f"Main Sentence: {sentence}")


