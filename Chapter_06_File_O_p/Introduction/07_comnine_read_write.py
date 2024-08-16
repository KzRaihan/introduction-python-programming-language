'''  
First read the file_07 message then use write() method using 'w+' mode

>> when we performs this 'w+' mode 
    -> first: truncated(remove all message)
    -> if we read() method : show nothing
    -> else we use write() method then new message is store in that file.


'''
# Open the file in write mode
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_07.txt", "w+") as f:
    data = f.read()
    print(data)

with open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\file_07.txt", "w+") as f:
    f.write("Hello Everyone\nToday Iam learning the file of i/o in python")

