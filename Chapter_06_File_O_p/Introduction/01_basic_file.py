'''     
Topic: file i/o in python: 

obj: perform file operation like reading, writing, deleting, renaming etc.

-> Type of file:
      1. Text file:
              --> .txt, .docx, .log etc
      2. Binary file:
              --> .mp4, .mov, png, jpg etc

-> we have to open a file before reading or writing

-> Syntax:
  file_object = open('filename', 'mode')
  
    here, 
        file object = similar to variable name
        open = keyword (to open the file)
        filename = name of the file or path of file
        mode = operation mode('r', 'w', 'a', etc)
        
                  
-> Basic file operations in python:
   1. read() : read all the content of file
   2. readline() : read one line at a time
   3. write(data) : write data to file
   4. close() : close the file
   5. rename(new_name) : rename the file
   6. remove() : delete the file

       

'''
# eg_01: we want to read ' First_01.txt' file

file = open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\First_01.txt", 'r')

data = file.read()

print(data)

print("Type: ", type(data))   # < class 'str' > 
# print("Type: ", type(file))

file.close()


