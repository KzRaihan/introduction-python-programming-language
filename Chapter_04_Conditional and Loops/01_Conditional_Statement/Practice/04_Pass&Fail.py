""" 
  WAP to find out whether a student has passed or failed if it require a total of 40% and
  at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user 

"""
num = []

num1 = int(input("\nEnter mark of subject one: "))
num.append(num1)

num1 = int(input("Enter mark of subject 2: "))
num.append(num1)

num1 = int(input("Enter mark of subject 3: "))
num.append(num1)

total_marks = sum(num)

percentage = (total_marks / 300) * 100

if(percentage>=40 and percentage>=30):
    print("Your pass: ",percentage)

else:
    print("Fail",percentage)




