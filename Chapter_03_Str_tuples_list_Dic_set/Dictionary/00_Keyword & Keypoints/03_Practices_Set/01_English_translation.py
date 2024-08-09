# WAP to create a dictionary of bangla words with values of their English translation.
# provide user with an option to look it up!

translation = {
    "ma" : "Mother",
    "baba": "Father",
    "vai" : "Brother",
    "bon" : "Sister",
    "dada" : "Grandfather",
    "dade" : "Grandmother",
    "kaka" : "Uncle",
    "kake" : "Aunty"
}

word = input("Enter you Bangla word: ")
print("Meaning of ", word, "is: ", translation[word])



