# list all 
list = ["Kz", 23, 90.25]
print(list)
print("Type : ", type(list))
print("length: ", len(list))

# indexing of list
print("\nFirst Element : ", list[0])
print("Second Element: ", list[1])
print("Thrid Element : ", list[2])

# modify of element
list[0] = "Raihan"
list[1] = 24
list[2] = 98.23
print("After modify the list: ", list)

# slicing of list
# access the part of sublist
print("\nAccessElement between 0 to 1 idx: ", list[0:2])
print("Access Element all idx: ",list[0:])
print("Element between 0 to length of list:  ",list[:len(list)])

# negative idx of access and slicing 
print("\nAccess list Element using negative idx ")
num = [10, 20, 30, 40, 50]
#      -5  -4  -3  -2   -1  <- idx
print("First element: ", num[-5])
print("Second element: ", num[-1])

print("Access Frist three element: ", num[-5:-2])

# Functionality or method of list
# list.append(element) this function return none 
# >> add element at the end of list
print("\nFunctionality or method of list")
main_list = [45, 15, 25, 71, 11]
print("Main list: ", main_list)
main_list.append(100)
print("\nAfter append                    : ", main_list)

# list.index(idx, element)
#  insert element at index
main_list.insert(2, 50)
print("\nAfter insert at idx 2           : ", main_list)

# list.sort() : sort in ascending order
# return none  
# change or sort for main list
main_list.sort()
print("\nsort in ascending               : ", main_list)

# list.sort(reverse = True) # here T is Chapital letter
# sort in reverse order
main_list.sort(reverse = True)
print("\nsort in descending order         : ", main_list)

# list.reverse():
# Reverse the list
main_list.reverse()
print("\nReverse list                    : ", main_list)

# list.remove(element):
# Remove the element of first occurence
main_list.remove(11)
print("\nAfter Remove element 11 in list: ", main_list)

# list.pop(idx)
# remove element at idx
main_list.pop(1)
print("\nPop the 1 idx                  : ", main_list)

# list.copy()
# copy the main list
copy_list = main_list.copy()
print("\nCopy list                      : ", copy_list)
print("\nMain list                      : ", main_list)


