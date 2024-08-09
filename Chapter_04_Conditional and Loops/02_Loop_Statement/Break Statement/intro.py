"""  
Topic: break statement in python
obj  : used to terminate the loop when encountered.
     -> exit inner and outer loop

"""
# eg_01: simple print 
i = 1
while i <= 10:
    if(i == 5):  # when i became 5 terminate the loop
        break
    print(i)    # o/p: 1 2 3 4
    i += 1

# eg_02: WAP to print search item(for first encountered) from given tuple
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49  # here x is search item
i = 0

while i < len(nums):
    if(nums[i] == x):      # here i use is idx
        print("search item is found at idx: ", i)
        break
    i += 1

    
""" 
         code explain : eg_02
         ======================
   here, search item x = 49
 
        1st iteration
       ----------------

   -> init: i = 0

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 0 < 11 (True)
        
        >> if_cds: nums[0] == 49       => search item = 49
                 => 1 == 49(False)
    
    -> inc = 0 + 1
           = 1  

        2nd iteration
       ----------------

   -> init: i = 1

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 1 < 11 (True)
        
        >> if_cds: nums[1] == 49       => search item = 49
                 => 4 == 49(False)
    
    -> inc = 1 + 1
           = 2  

        3th iteration
       ----------------

   -> init: i = 2

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 2 < 11 (True)
        
        >> if_cds: nums[2] == 49       => search item = 49
                 => 9 == 49(False)
    
    -> inc = 2 + 1
           = 3  
        4th iteration
       ----------------

   -> init: i = 3

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 3 < 11 (True)
        
        >> if_cds: nums[3] == 49       => search item = 49
                 => 16 == 49(False)
    
    -> inc = 3 + 1
           = 4  
        5th iteration
       ----------------

   -> init: i = 4

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 4 < 11 (True)
        
        >> if_cds: nums[4] == 49       => search item = 49
                 => 25 == 49(False)
    
    -> inc = 4 + 1
           = 5  
        6th iteration
       ----------------

   -> init: i = 5

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 5 < 11 (True)
        
        >> if_cds: nums[5] == 49       => search item = 49
                 => 36 == 49(False)
    
    -> inc = 5 + 1
           = 6  

        7th iteration
       ----------------

   -> init: i = 6

   -> while_cds: i < len(nums)         => len(nums) = 11
               = 6 < 11 (True)
        
        >> if_cds: nums[6] == 49       => search item = 49
                 => 49 == 49(True)
        print: search item is found at idx: ", i  => i = 6

            >> break     => this break statement means terminate the loop
     

final o/p: search item is found at idx : 6

"""