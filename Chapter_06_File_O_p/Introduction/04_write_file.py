'''   
Write() method use:
 -> Write() method is used to write a string to a file.
 -> Truncate(overwrites) the entire file

> Syntax:
   1. file_object.write(string)

   2. with("file path", "w") as f:
        -------------
        f.write(string)     
        -------------
    here,
       w = write mode
    
   
 -> If the file does not exist, it creates the file(automatic) then write messages or somethings



'''
# eg_01: write an file and store this value of demo.txt file
f = open("R:\\introduction python programming language\\Chapter_06_File_O_p\Introduction\\04_demo.txt", "w")

f.write("This is the new data")
f.close()

# eg_02 : using 'with' syntax to perform write() method

with open("R:\introduction python programming language\Chapter_06_File_O_p\Introduction\demo_04.txt", "w") as f:
    f.write("Change your mind \n\tand\n") 
    f.write("Change your life\n") 
  

