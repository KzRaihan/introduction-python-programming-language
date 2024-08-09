""" 
Topic: cds type in loops

type: there two type of conditions
    >> 1. single type value
    >> 2. comparison type value

1. single type value:
   -> most use when we can't know the how many times loop counter are run.
   
   ->syntax:
      while(single value):
           ---------
           statements # work
           --------
  -> for single values:
      >> False cds: 0(zero) and False(which is boolean value) 
      >> True cds: Except 0(zero) and False all values are True  
 """
 # 1. single type value 
# eg_01
print("\nExample:_01: print Hello 5 times\n")

i = 5  # ini part || loop counter or iterator
while i: # (T) 5 is not  zero(0)
    print("Hello")
    i -= 1

# eg_02:
print("\nExample:_02: print 10 to 1\n")
i = 10
while(i):
    print(i)
    i -= 5

# # eg_03: -> this is infinite loop
# while(True):
#     print("I am Kz")

# eg_04: for increment loop counter
print("\nExample:_04: negative numbers print \n")
count = -5
while count:
    print(count)
    count += 1


"""  
     Code explain with eg_01


     1st iteration
     ---------------

>> init: i = 5

>> cds : i
       = 5 (True)

>> Body: print : Hello

              o/p: Hello

>> update(Decrement): 
             i = i - 1
               = 5 - 1
               = 4

     2nd iteration
     ---------------

>> init: i = 4

>> cds : i
       = 4 (True)

>> Body: print : Hello

              o/p: Hello
              o/p: Hello

>> update(Decrement): 
             i = i - 1
               = 4 - 1
               = 3
     3th iteration
     ---------------

>> init: i = 3

>> cds : i
       = 3 (True)

>> Body: print : Hello

              o/p: Hello
              o/p: Hello
              o/p: Hello

>> update(Decrement): 
             i = i - 1
               = 3 - 1
               = 2
            
     4th iteration
     ---------------

>> init: i = 2

>> cds : i
       = 2 (True)

>> Body: print : Hello

              o/p: Hello
              o/p: Hello
              o/p: Hello
              o/p: Hello

>> update(Decrement): 
             i = i - 1
               = 2 - 1
               = 1
     5th iteration
     ---------------

>> init: i = 1

>> cds : i
       = 1 (True)

>> Body: print : Hello

              o/p: Hello
              o/p: Hello
              o/p: Hello
              o/p: Hello
              o/p: Hello

>> update(Decrement): 
             i = i - 1
               = 1 - 1
               = 0
     6th iteration
     ---------------

>> init: i = 0

>> cds : i
       = 0 (False cds)

>> end of loop

     final o/p:
            Hello
            Hello
            Hello
            Hello
            Hello
            
"""