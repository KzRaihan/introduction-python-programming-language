"""
Definition: 
    refers to using conditional statements inside another condition statement.
Syntax: 
      if(cds):   # outer if condition
         if(cds):  # inner if cds
          -----------
          -----------
          statements
          -----------
          else:   # inner else cds
            ---------
            statements
            ----------
      else:     # outer else cds
         -------
         -------
         statements
         ----------
"""
# eg_01
age = int(input("Enter age: "))

if(age >= 18):   # outer if cds
    if(age >= 80):  # inner if cds
        print("Can't Drive")
    else:           # inner else cds
        print("Can Drive")
else:            # outer else cds
    print("\nNot Adult")
    print("Can't Drive")