# WAP to detect double space in a string and replace the double space to single space

# eg_01
name = "Md  Kamruzzaman Raihan"
idx_dou_space = name.find("  ")
print("Double space idx: ", idx_dou_space)

print("Recover double space to single space: ",name.replace("  ", " "))   # this replace() return new string 

print("Main string: ",name)   # Main string can't change 