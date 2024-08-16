'''   
tell(): Return the file handler(pointer) position.
'''
# with open("four", "x") as f1:      # create a file(four)
#     f1.write("something")   # write message 

with open("four", "r+") as f2:  # open file in both and pointer position at the beginning
    print(f2.tell())   # first position: 0

    print(f2.read())        # display message in console if mess is exists

    print(f2.tell())     # count the pointer position: 9

    f2.write("How are you")  # write message and after perform the pointer position is (v)

    print(f2.tell())    # count the pointer position: 20

