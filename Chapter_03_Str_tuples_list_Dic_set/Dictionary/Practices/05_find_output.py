# what will be length of following set s:
#   s = set()
#   s.add(30)
#   s.add(30.0)
#   s.add("30")

s = set()
s.add(30)
s.add(30.0)       # In Python, integers and floats are considered equal
                  # if they have the same value, even if they are different types.

s.add("30")

length = len(s)
print("Length: ", length)

