# All useful or most use list method in python
#     -> list method modify the original list

# 1. append(el): Add element at the end of list
nums = [20, 10, 50, 40, 30, 70, 80, 60, 90] 
print("Original list: ", nums)

nums.append(100)   # add 100 at the end of nums
print("\nAfter append() perform : ", nums)  # original list is update

# 2. insert(idx, el)  -> according to idx add the element

nums.insert(2, 50)   # add 50 at the 2nd position of nums
print("\nAfter insert() perform : ", nums)  # original list is update

# 3. sort()   -> sort the list in ascending order
nums.sort()

print("\nAfter sort() perform : ", nums)  # original list is update

# 4. reverse() -> reverse the list

nums.reverse()
print("\nAfter reverse() perform : ", nums)  # original list is update

# 5. pop(idx) -> according the idx pop the element

nums.pop(2)  # pop 80 at the 2nd position of nums (here, nums is reverse)
print("\nAfter pop() perform : ", nums)  # original list is update

pop_el = nums.pop(1) # 90 is pop
print("\npop Element in nums: ", pop_el)

# 6. remove(el)   -> direct remove the element in list
nums.remove(50) # 50 is remove if it is present in nums list

print("\nAfter remove() perform : ", nums)  # original list is update

# 7. copy() : -> copy the original list(nums)
nums.copy()
print("\nAfter copy() perform : ", nums)  # original list is copy

# 8. clear() -> remove all the elements from the list(nums)

nums.clear()
print("\nAfter clear() perform : ", nums)  # original list is clear
