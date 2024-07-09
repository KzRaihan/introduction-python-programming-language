"""  
 Topic : list.insert() function
 obj   : add or insert one element at the giving idx

    - list.insert return the None value

 -> Syntax: 
     list_name.insert(idx, element)
"""
# eg_01
product = ["Shirt", "Jeans", "Suit", "Hoodie"]

# insert T-Shirt into idx 1
product.insert(1, "T-Shirt")
print(product)

# eg_02
num = [5, 15, 35, 45, 65]
num.insert(2, 25) # 2 idx to add 25
print(num)

print(num.insert(5, 55)) # o/p: None but insert 55 into 5 idx
print(num) 

# eg_03: insert element into 0 idx
num.insert(0, 10)
print(num)

# eg_04: input list form user and then insert an element

user_list = list(map(int, input("Enter numbers separated by space: ").split()))
insert_num = int(input("Enter number to insert: "))
insert_idx = int(input("Enter index to insert: "))

user_list.insert(insert_idx, insert_num)       