"""  
WAF to print the length of a list (list is the parameters)
           
"""
def length_list(nums): # <- called function. here, nums received all form list.
    len1 = len(nums)
    return len1


list = [10, 20, 30, 40, 50, 60]

for el in list:
    print(el, end = " ")

result = length_list(list) # <- calling function
print("\nLength is :",result)

"""   
         code explain

    list = [10, 20, 30, 40, 50, 60]

    for loop:
               1st iteration
             --------------
       ->  el = list[0]
           el = 10
       -> print: el 
                = 10
         -> end of statement is change : " " 
       
               2nd iteration
             --------------
       ->  el = list[1]
           el = 20
       -> print: el 
                = 20                   
         -> end of statement is change : " " 


        according this process until all list elements print
        then o/p:
                10 20 30 40 50 60
  
  > calling function: length_list(list) 
      -> calling function pass the list to called function
      -> control is pass the called function
      -> when return the value from called function then show the output
  
  > called function : def length_list(nums)
      -> called function parameter nums received the arguments of calling function which list
      -> Calculated the length using len function
                        and
      -> return the len to called function  


"""