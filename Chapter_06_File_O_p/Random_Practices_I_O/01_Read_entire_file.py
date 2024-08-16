# read() method to print entire message form demo.txt file using function

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# path(variable) is sore the path of demo.txt file
path = "R:\introduction python programming language\Chapter_06_File_O_p\Random_Practices_I_O\demo.txt"

message = read_file(path)

print(message)          # this is provide the all text in demo.txt file
print(type(message))    # < str > || we know the file is always return a stream of character that way(str)


print(type(path))   # < str > file path is string that way (str)

