# WAP to accept marks of 6 students and display them in sorted manner

marks = []

s1 = float(input("Enter your marks: "))
marks.append(s1)


s2 = float(input("Enter your marks: "))
marks.append(s2)

s3 = float(input("Enter your marks: "))
marks.append(s3)

s4 = float(input("Enter your marks: "))
marks.append(s4)

s5 = float(input("Enter your marks: "))
marks.append(s5)

s6 = float(input("Enter your marks: "))
marks.append(s6)

print("\nMarks of 6 Student: ", marks)

# sort this marks in ascending order
marks.sort()
print("\nStored marks : ", marks)