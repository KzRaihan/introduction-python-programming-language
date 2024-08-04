"""  
WAF to convert USD to Tk
   hint: 1 USD = 124 Tk
"""
def USD_TK(usd):  # called function with return value
    convert = usd * 124
    return convert

us = int(input("\nEnter the USD Account: "))

tk = USD_TK(us) # calling function with pass argument
print(us, "USD is equal: ", tk, "Taka")