'''    
Topic: append() method 
     -> adds to the file at the end
     -> can't overwrite file (add new file at the end)
     -> if file not exist it will create file then append

 > 1.Normal 
    f = open('sample.txt', 'a')

    f.write('This is appended data')  # for new line

> 2. with syntax:
    with open("file path", "a") as f:
        f.write("append this message at the end")  # for new line
 

'''

# 1. Normal
f = open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\demo_04.txt", "a")
f.write("Break your comfort zone\n")

f.close()  # close the file after writing. it's good practice to close file after use.

# 2. using with syntax: to append some data
with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\demo_04.txt", "a") as file:
    file.write("and stay focused\n")