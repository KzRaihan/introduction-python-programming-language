#  create an empty dictionary allow 4 friends to enter their favorite language as value and use key as their names.
# assume that the names are unique

fv_lang ={}  # empty dic


name = input("\nEnter first friend name: ")
lang = input("Enter language: ")
fv_lang.update({name: lang})

name = input("\nEnter second friend name: ")
lang = input("Enter language: ")
fv_lang.update({name: lang})

name = input("\nEnter Third friend name: ")
lang = input("Enter language: ")
fv_lang.update({name: lang})

name = input("\nEnter four friend name: ")
lang = input("Enter language: ")
fv_lang.update({name: lang})

print("\nFriend's favorite languages: ", fv_lang)
