'''  
mode: r+
> open file in both read and write
> file handler exists at the beginning.
> arise error if file doesn't exist

NNB: when we perform or terminal multiple time it will generate an multiple times message

'''
# eg_01: file is already exists
with open("third", "r+") as f1:  # this line open file in r+(read and write) mode
    data = f1.read()   # all message store in data and pointer position at the end
    print(data)  # display in console

    f1.write("this is new data") # write message start with where pointer position is end previously after perform write() pointer position is at the end
    print(f1.read())  # read start with when the position of pointer (now pointer position at the end) | so, line provide no output 

with open("third", "r+") as f2:  # this line open file in mode r+ and pointer position at beginning
    print(f2.read())  # read all message exists in third file





