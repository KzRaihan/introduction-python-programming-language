# eg_02: read the file simple_02
'''  
read file syntax:                                   NNB: first -> open, then perform different operations
------------------
  1. with syntax:
     with open(file_name, 'r') as file_obj:
    
  2. in general:
     file = open("path of the file or file name", "r")

     open = keyword or it's a function
     r    = mode of read the file
     file_obj = object name for file
     
'''
# eg_01: use in general syntax: to read the simple_02.txt file

f = open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\simple_02.txt", "r")

data = f.read()

print(data)

f.close()  # close the file after reading it. it's good practice to close file after use.

# using with syntax to solve this same problem
with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\simple_02.txt", "r") as f:
    print(f.read())

# when use with syntax we do not need close() method
