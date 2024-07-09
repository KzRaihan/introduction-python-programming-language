"""  
 Topic : list.append() function
 obj   : add one element at the end

    - list.append return the None value

 -> Syntax: 
     list_name.append(element)
"""
# eg_01
list = [15, 25, 35, 45, 55]
print(list.append(65)) # o/p: none but 65 is add in list at end
print(list)

# eg_02 
str = ["Kz", "sk", "SR"]
str.append("Rai")
print(str) # o/p: ['Kz', 'sk', 'SR', 'Rai']
