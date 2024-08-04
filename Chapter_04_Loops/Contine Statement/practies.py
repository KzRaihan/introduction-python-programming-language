""" 
-> print all numbers from 1 5o 10 except 8.
"""
i = 1
while i <= 10:
    if(i == 8):
        i += 1
        continue
    print(i)
    i += 1