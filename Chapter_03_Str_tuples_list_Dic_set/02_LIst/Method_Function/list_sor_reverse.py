""" 
# Topic: list.sort(reverse=True or False) function

#  obj1: when use list.sort(reverse=True)
      >> list sort in descending order

# obj2: when use list.sort(reverse=False)
      >> list sort in ascending order
"""
# obj1: list.sort(reverse=True)
name = ["Apple", "apple", "kz","Dhaka", "1234", "40.236", "Raihan"]
# name.sort(reverse=True)
# print("Name list sort in reverse order: ", name)

# obj2: list.sort(reverse=False)
name.sort(reverse=False)
print("Name list sort in ascending order: ", name)


""" 
Explain_code: 
          name.sort(reverse=False)
    >>> String are compare character by character 
        Eg: here: let(first string Apple) A = smaller then compare the
         second (string apple) a
      
    - first compare
         A < a (True)
        how it true 
        A ASCII value = 65
        a ASCII value = 97
        so, "Apple" is smaller than "apple"
    - second compare
        A < k (True) here, A = 65, k = 107
        so, "Apple" is still smaller than "kz"
    - third compare
        A < D (True) here, A = 65, D = 68
        so, "Apple" is still smaller than "Dhaka"
    - Four compare
       A < 1 (false) here, A = 65, 1 = 49
   ***   so, 1 is smaller than A
    - Five compare
        1 < 4(True) here, 1 = 46, 4 = 52
        so, 1 is still smaller than 40.236
    - six compare
        1 < R (True) here 1 = 46 , R = 82
        so, 1 is still smaller than Raihan

        so, final first o/p: 1234

    similar to compare another and output
    [  1234 , 40.236, Apple, Dhaka, Raihan, apple, kz ]
      
              
"""