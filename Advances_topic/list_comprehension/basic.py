'''
Topic: Comprehension in python:

- Definition: 
      Comprehension in python, are Syntactic(grammatical) constructs that allow for the concise creation of collections. like(list, dictionary, sets)


- Type of Comprehension:
    -> List comprehension
    -> Dictionary comprehension
    -> Set comprehension
    -> Generator expression

- Why use comprehension:
      Provide a more readable and concise way to create collections.

    key points that highlight:
    - Conciseness and readability.
    - Improve Performance.
    - Filtering with conditions.
    - Efficiency memory usage.
    
   Comprehension is more faster then the traditional methods(loop).

- Disadvantages:
    - Limited Debugging Capability.
    - Complexity in Nested Comprehension.

-1. List Comprehension:
       offers a concise way to create a new list based on existing list, range or other sequences.

    --Syntax:
        new_list = [expression  for item in iterable   if condition]

    here, 
         new_list = Return new list
         expression  = output(Execute part)
         collections = for item in iterable
         condition = filter condition(optional)


'''
# eg_01: Simple list comprehension(loop vs list comprehension)
result = []

for i in range(10):
    result.append(i)

print(result)

# using list comprehension
new_list = [i for i in range(10)]
print(new_list)

# eg_02: Square of each elements in existing list.
nums = [1, 2, 3, 4, 5]

# using for loop
square_nums = [] # empty list
for i in nums:
    square_nums.append(i*i)

print(square_nums) 

# using list comprehension
squ_nums = [i * i  for i in nums]  # concise way to create and easier to understand

print(squ_nums)  

# eg_03: Filtering Even numbers for a list (by using condition part)
even_nums = [n for n in nums if n%2 == 0]

print("Even numbers: ", even_nums)

# eg_3.1: Generating list of a square of even numbers
squ_even_nums = [n*n for n in nums if n%2 == 0]
print("Square of even numbers: ", squ_even_nums)


# eg_04: if... else with list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_odd_nums = ["Even" if i%2 == 0 else "Odd" for i in numbers]
print(numbers)
print(even_odd_nums)

# another way 
even = []
odd = []

e_o_nums = [even.append(n) if n%2==0 else odd.append(n)  for n in numbers]

print("Even numbers: ", even)
print("Odd numbers: ", odd)

# eg_05: Flattening a list of lists(Nested loop)

list = [[1, 2,3], [4, 5, 6], [7, 8, 9], [10]]

flat_list = [item for sublist in list for item in sublist]
print(flat_list)


# eg_06: Flattening with filtering
lst = [[1, 'a', 2], [3,'b', 4], [5]]

flat_lst = [n for sublist in lst for n in sublist if isinstance(n, int)]
print(lst)
print(flat_lst)

# eg_07: find even numbers(1-100) that are divisor by 5
divisor_even = [num for num in range(1, 101) if num %2 == 0]
print("Divisor Even numbers: ",divisor_even)

# eg_08: Generating a list of all divisors of a number.(assume num = 36)
num = 36
divisor_nums = [i for i in range(1,num+1) if num%i == 0]
print("All divisor: ", divisor_nums)

# eg_09: converting a list of string to a list of integer
str_lst = ['1', '2', '3', '4', '5']

int_lst = [ int(strl) for strl in str_lst]

print("str to int: ", int_lst)
print("type: ", type(int_lst[0]))

# eg_10: Generating  a list of the first letters of words in a list

fruits = ["apple", "banana", "cherry", "date"] 
first_letters = [ f[0] for f in fruits]
print(first_letters)

# convert smaller case to upper case letter of fruits names

Cap_fruits = [ fruit.upper()  for fruit in fruits]
print(Cap_fruits)


# eg_11: Generating a list of the fibonacci sequence using a list comprehension
fib = [0,1, 1, 2, 3, 8,13, 21, 34, 54, 89, 144, 233, 377]

fib_nums = [fib[i-2] + fib[i-1] for i in range(2, len(fib))]
print(fib_nums)

# # eg_12: 
# my_str = "MyNameIsKzRaihan"

# my_str = [i if i.islower() else " " + i for i in my_str]
# print(my_str)