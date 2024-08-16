'''   
Create an file using mode: x
> when run first time it will create 
> when run second time the same file name it will generate error

'''
# eg_01: create an text file name first.txt and write some text

with open("first", "x") as f1:     # this line create an file name first.txt 
    f1.write("This is the person\n")  # this line write the text : This is the person

# eg_02: then this same code perform again that will generate error
# because of file name can't same name
    