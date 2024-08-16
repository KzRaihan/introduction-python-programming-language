'''   
mode : r
    -> Opens file in read mode. The file pointer is placed at the beginning of the file. 
    -> If the file does not exist, an IOError is raised.
    -> This is the default mode

'''

# eg_01: read a file and print its content on console
with open("first","r") as f1:
    print(f1.read())

# if we can't provide any mode then it will provide same output(print in console)
print("\nIn Default mode access the data: ")
with open("first") as f2:
    data = f2.read()

    print(data)

# if we use write operation it's will generated error
with open("first", "r") as f3:
    f3.write("this is write operation..")  # this line generated error(we can't write() in 'r' mode)
