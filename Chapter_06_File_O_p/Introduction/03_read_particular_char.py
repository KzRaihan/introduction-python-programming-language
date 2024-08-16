'''   
We want to print particular set of character in a file form simple_02.txt file
'''

# eg_01 : Read the entire file
print("\nExample 1: ")

with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\simple_02.txt", "r") as f:

    data = f.read()
    print(data)


# eg_02 : Read first 10 character
print("\nExample 2: ")

with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\simple_02.txt", "r") as f:

    data_first_10 = f.read(10)  # 10 means first 10 character
    print(data_first_10)

# eg_03: Read first line form First_01.txt file
print("\nExample 3: ")
  
with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\First_01.txt", "r") as f:
    data_first_line = f.readline()
    print(data_first_line)

# eg_04: Read line by line using readline() form First_01.txt file
print("\nExample 4: ")

with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\First_01.txt", "r") as f:
    line_01 = f.readline()
    print(line_01)

# eg_05: Read all line form First_01.txt file 
print("\nExample 5: ")

with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\First_01.txt", "r") as file:
    for line in file:
        print(line)

print("\n")
