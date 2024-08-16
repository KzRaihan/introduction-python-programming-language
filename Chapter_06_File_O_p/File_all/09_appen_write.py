''' 
mode: a+ (write and append) and can't read 
> write message at the end
> file pointer position at the end

'''
# with open("five", "x") as f1:
#     f1.write("Listen to me")

with open("five", "a+") as f1:
    f1.write("\nOpen the computer")  # file pointer position at the end of file

# with open("five", "a+") as f2:
#     print(f1.read())  this will generate error message

with open("five", "r+") as f3:
    print(f3.read())  # this line have no output because the position of the file pointer
    print("file pointer position: ", f3.tell())

    f3.write("\nBye Everyone for file in i/o")
    f3.seek(0)
    print(f3.read())  # this line will print the content of the file

