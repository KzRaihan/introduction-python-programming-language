'''   
append(a+) mode:
  first: open file
  second: write data at the end 

'''
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_07.txt", "a+") as f:
    f.write("Iam from Bangladesh \nIam 23 Years old.")

f.close()

with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_07.txt", "a+") as f:
    data = f.read()
    print(data)    # for this read operation show nothing because the pointer is pointing at the end for first f.write() operation.

