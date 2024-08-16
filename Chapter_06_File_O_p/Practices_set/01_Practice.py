'''  
> Create a new file "Practice.txt" using python and add the following dat in it
    Hi everyone
    We are learning file i/o
    using java
    I like programming in java
'''
# first way to add using r+ mode
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\\Practices_set\\demo_01.txt", "r+") as f:
    f.write("Hi everyone\n")
    f.write("We are learning file i/o\n")
    f.write("using java\n")
    f.write("I like programming in java\n")

# second way to add using a+ mode
with open("R:\\introduction python programming language\\Chapter_06_File_O_p\\Practices_set\\demo_01.txt", "a+") as f:
    f.write("\nHi everyone\n")
    f.write("We are learning file i/o\n")
    f.write("using java\n")
    f.write("I like programming in java\n")
