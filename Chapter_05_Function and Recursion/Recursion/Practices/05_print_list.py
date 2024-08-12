# WARF to print all element in a list . (Hint: use list and index as parameters)

def Access_element(list, idx=0):
    if idx < len(list):
        print(list[idx], end = " ")
        Access_element(list, idx + 1)
    else:
        return




list = ["Kz", "Raihan", "sk", "RR"]

Access_element(list)