"""  
You are given a list of subjects for students. assume one classroom is require for 1 subject. 
how many classroom are needed by all students

 "python", "java", "c++", "python", "javascript", "java", "python", "java", "c+", "c".

"""
subject_set = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print("Subject are: ", subject_set)
length = len(subject_set)
print("\nClassroom need: ", length)

""" 
Explanation:
   >> we know, set are remove the duplicate values
   >> if multiple subject are same then set ignore the duplication(count one time)
   >> then we count the length of the set which gives the number of unique subjects that is the classroom need.
"""
