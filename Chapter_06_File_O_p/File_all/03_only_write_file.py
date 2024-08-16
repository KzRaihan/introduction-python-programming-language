'''  
mode: 'w'
  > open file in write mode
  > It overwrite the file if file already exists, if file doesn't exists it will create a new file.
  > The file handler exists at the beginning.
'''
# eg_01: file does not exists
with open("second", "w") as f1:  # this line generate a new file name second
    f1.write("Create a file second")  # in second file write message(This is new file)

# eg_02: file is already exist in file (so, second file is exists now)
with open("second", "w") as f2: # this line remove old data in file 'second'
    f2.write("This is the new data in file second") # this line write a new message(This is the new data in file second)

# eg_03: generate an error (when we read the file )
with open("second","w") as f3:     # this line remove old data 
    print(f3.read())  # this line generated error(because file can't read in 'w' mode)