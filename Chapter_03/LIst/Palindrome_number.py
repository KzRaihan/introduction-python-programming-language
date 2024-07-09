""" 
WAP to check if a list contains a palindrome of elements

  >> A list is palindrome if the main list reverse then output the same (main list) then it's called list is palindrome.
"""
list = ["Kz", 4039, "Kz"]
print("Main list: ", list)

copy_list = list.copy() # copy the main list

copy_list.reverse() # reverse the copy list

if(list == copy_list): # compare list and reverse copy list 
    print("List is Palindrome")
else:
    print("List is not Palindrome")