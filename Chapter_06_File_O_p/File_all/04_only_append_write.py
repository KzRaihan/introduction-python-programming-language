'''   
Mode: a
 > open file in append/write mode
 > file handler exists at the end(if file previously written or if file already exists)
 > if file doesn't exists then create a new file 
 > newly written data will be added at the end of the file.

'''
#  eg_01: file does't exists 
with open("third", "a") as f1:  # this line crate a new file (third)
    f1.write("Hello")   # this line write 'Hello' in newly create file (third)

# eg_02: when file is already exists
with open("third", "a") as f2: # this line open the third file
    f2.write("Everyone")     # write 'Everyone' at the end in third file

# eg_03: Generate error when open file in append mode and read something
with open("third", "a") as f3:
    print(f3.read())    # this line generate an error 
