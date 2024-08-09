#  create an empty dictionary allow 4 friends to enter their favorite language as value and use key as their names.
# if the language of 2 friends are same; what will happen to the program in problem 2


# we know that key value can be anything
# key value can be same that is no problem

em_dic = {}

name = input("\nEnter first friend name: ")
lang = input("Enter language: ")
em_dic.update({name: lang})

name = input("\nEnter second friend name: ")
lang = input("Enter language: ")
em_dic.update({name: lang})

name = input("\nEnter thrid friend name: ")
lang = input("Enter language: ")
em_dic.update({name: lang})

name = input("\nEnter four friend name: ")
lang = input("Enter language: ")
em_dic.update({name: lang})

print("\nAll friend and language: ", em_dic)
