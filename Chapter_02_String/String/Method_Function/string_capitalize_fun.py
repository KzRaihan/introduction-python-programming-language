"""
  Topics: string capitalize()
  Summary: This function converts the first character of a string to uppercase.

  Syntax:
     string_name.capitalize()
"""
city = "dhaka is capital of bangladesh\n"  # here, city is the string name

print(city.capitalize())  # output: Dhaka is capital of bangladesh
# in this way it can't change the original string 

print(city)  # output: dhaka is capital of bangladesh

# Permanent change the original string

city = city.capitalize()
print(city)  # output: Dhaka is capital of bangladesh
