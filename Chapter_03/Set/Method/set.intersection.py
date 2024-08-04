"""   
Topic: set.intersection(set2) method
obj  : combines common values and return new set

Syntax:
    set1_name.intersection(set2_name)
"""
# eg_01
collection_1 = {1, 2, 3}
collection_2 = {3, 4, 5}

print(collection_1.intersection(collection_2))  # {3}

# eg_02
set1 = {"Kz", "Raihan", "Dhaka", "Bangladesh", 4039}
set2 = {"Rahim", "Raihan", "Dhaka", "Bangladesh"}

set3 = set1.intersection(set2)
print("\nset_03: ", set3)  # {'Raihan', 'Dhaka', 'Bangladesh'} only common values in set1 and set2
