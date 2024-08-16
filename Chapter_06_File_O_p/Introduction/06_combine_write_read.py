'''  
> combine read() and write() using 'r+' mode


'''
# eg_01: first write message then read in file_06.txt
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_06.txt", "r+") as f:
    f.write("My Name is KzRaihan\n")
    f.write("I'm 23 years old")

with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_06.txt", "r+") as f:
    print("\nfile_06 within message: \n")
    print(f.read())

# eg_02: first overwrite message then read in file_06.txt
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_06.txt", "r+") as f:
    f.write("My favorite sport")

with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_06.txt", "r+") as f:
    print("\nfile_06 within message: \n")
    print(f.read())
