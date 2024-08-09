# Mark Distribution Problem
"""
    >> if      mark   || Letter Grade || Range

             -> 80-99 || A+           || 4.00
             -> 75-79 || A            || 3.75
             -> 70-74 || A-           || 3.50
             -> 65-69 || B+           || 3.25
             -> 60-64 || B            || 3.00
             -> 55-59 || B-           || 2.75
             -> 50-54 || C+           || 2.50
             -> 45-49 || C            || 2.25
             -> 39-44 || D            || 2.00 
             -> 0-39  || F            || 0.00
          
"""
mark = float(input("Enter Your Mark: "))
if(mark>=100 or mark<0):
    print("Invalid Mark")
elif(mark>=80):
    print("Letter Grade : A+", "\tRange: 4.00")
elif(mark>=75):
    print("Letter Grade : A", "\tRange: 3.75")
elif(mark>=70):
    print("Letter Grade : A-", "\tRange: 3.50")
elif(mark>=65):
    print("Letter Grade : B+", "\tRange: 3.25")
elif(mark>=60):
    print("Letter Grade : B", "\tRange: 3.00")
elif(mark>=55):
    print("Letter Grade : B-", "\tRange: 2.75")
elif(mark>=50):
    print("Letter Grade : C+", "\tRange: 2.50")
elif(mark>=45):
    print("Letter Grade : C", "\tRange: 2.25")
elif(mark>=39):
    print("Letter Grade : D", "\tRange: 2.00")
else:
    print("Letter Grade : F", "\tRange: 0.00")
    
   

