'''  
Search if the the word 'learning' exists in the demo_02.txt file or not.
learning

'''
def search_item(path):
    idx = 0
    with open(path,'r+') as f:
        data = f.read().lower()
        idx = data.find("learning")
        return idx

        # if(data.find("learning")):
        #     return "learning is found"
        # else:
        #     return "learning is not found!"
       



path = "R:\introduction python programming language\Chapter_06_File_O_p\Practices_set\demo_03.txt"

ans = search_item(path)
print(f"learning is found at idx: {ans}") 