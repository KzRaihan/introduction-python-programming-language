'''  
WAF the replaces all occurrences of 'java' with 'python' in demo_02.txt file
'''

def replace_data(path):   # definition of replace_data or called function
    with open(path, "r") as f:
        data = f.read()
        new_data = data.replace("java", "python")
        print(new_data)
    
    with open(path, "w") as f:
        f.write(new_data)

def replace(path):
    with open(path, "r+") as f:
        # read data from file
        data = f.read()
        update_data = data.replace("We are", "I am")

        # write data to file
        f.write(update_data)


        
        
path = "R:\introduction python programming language\Chapter_06_File_O_p\Practices_set\demo_02.txt"

replace_data(path) # calling function

print("For second replace function: \n\n")

replace(path)


'''  




'''