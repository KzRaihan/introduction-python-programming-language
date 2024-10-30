# first find all numbers in the given lst
# then square the numbers then find the even numbers and for all even numbers following (2*even_numbers - 10) expression.
lst = ["kz", 98, 99, 100, "Ra", 40, 45, 50, "Sk", 10, 15, 20, "Rahim", 70, 75, 80, "Rakib", "Rana", "Raju", 90, 12, 35, ]


# first find all numbers in the given lst
nums = [num for num in lst if isinstance(num, int)]
print(nums)

# then square the numbers in the given lst then calculate even numbers and also calculate (2*even_numbers - 10) expressions
expression = [(2*even - 10) for even in [n**2 for n in nums ] if even%2 == 0]

print(expression)



# to convert celsius  to fahrenheit  (formula : f = c*9/5 + 32)
cal = nums
print("Celsius Temperatures: ",cal)

far = [ (c*9/5 + 32)   for c in cal]
print("Fahrenheit Temperatures : ", far)