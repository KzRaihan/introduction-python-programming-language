'''   
topic: seek()

obj  : The seek() method changes the current position of a file object or file handler or file pointer.

'''
# eg_01: 
with open("four", "r+") as f1:
    data = f1.read()
    print(data)
    print("Current position: ", f1.tell())  # print current position of file pointer which is : 20

    f1.seek(0)  # here, change or modify the file pointer position 20 to 0 . n
    print("After seeking to 0: ", f1.tell())  # print current position of file pointer which is : 0

    f1.write("May Almighty bless you")
    print("After write: ", f1.tell())  # after perform write operation file pointer position: 24

    