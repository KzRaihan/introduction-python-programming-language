'''   
mode: w+ 
> file open in both write and read mode
> file pointer position at the beginning.
> overwrite all message which is exists in file already
'''
with open("four", "w+") as f1: # open file both : read and write
    print(f1.tell())  # return the current position of file pointer
    f1.write("This is a new message in file four") # write some message in file (four)
    print(f1.tell()) # return the current position of file pointer

    f1.seek(0)  # change the file pointer position now it is 0 position
    print(f1.read()) # now read file first to last
