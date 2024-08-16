# search the item input from user which is the file demo.txt or not
def search_item(path, item):
    with open(path, "r+") as file:
        data = file.read()
        val = item.lower()   # convert item into lower case
        val2 = data.lower()  # convert file message into lower case
        

        idx = val2.find(val)  # find the idx of val which is existing in val2 
        # print(idx)
        if (idx != -1):  # -1 means if idx is not found or search item is not in the file(demo.txt)
            print(f"Item '{item}' found in the at idx: {idx}")
        else:
            print(f"{item} is not found!")
        
           


path = "R:\introduction python programming language\Chapter_06_File_O_p\Random_Practices_I_O\demo.txt"

item = input("Enter your search string: ")

search_item(path, item)