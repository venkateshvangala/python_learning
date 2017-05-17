# Normal list to create squares of upto given range 
n = int(input("enter range: "))
squares = []
for x in range(n):
    squares.append(x ** 2)
print("Squres upto given number: ", squares)
print("x value wont be destroy in this case: ", x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Comprehensions list to create a Squares (Lambda expression)
squares.clear()
squares = list(map(lambda x: x ** 2, range(10)))
print("Squres upto given numbers using lamba: ", squares)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

squares.clear()
squares = list(x ** 2 for x in range(10)) # Equivalent to [x ** 2 for x in range(10)]
print("Squres upto given numbers using comprehensions: ", squares)


#  using comprehension listcomp combines the elements of two lists if they are not equal
listComp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("listcompo using comprehensions is as follows: ")
print(listComp)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# create a new list with the values doubled
vec = [-4, -2, 0, 2, 4]
list = [x ** 2 for x in vec]
print("comprehensions to return dobuled the values of list")
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# filter the list to exclude negative numbers
list.clear()
list = [x for x in vec if x >= 0]
print("list with positive numbers:")
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# apply a function to all the elements
list.clear()
list = [abs(x) for x in vec]
print("apply a function to all elements: ")
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# create a list of 2-tuples like (number, square)
list.clear()
list = [(x, x ** 2) for x in vec]
print("create a list of 2-tuples like (number, square)")
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# the tuple must be parenthesized, otherwise an error is raised
list.clear()
# list = [x, x ** 2 for x in vec]
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
list.clear()
list = [num for elem in vec for num in elem]
print('flatten a list using a listcomp with two for')
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# List comprehensions can contain complex expressions and nested functions:

from math import pi
list.clear()
list = [round(pi, i) for i in range(1, 6)]
print('List comprehensions can contain complex expressions and nested functions: ')
print(list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list.clear()
list = [[row[i] for row in matrix] for i in range(4)]
print(list)

# you can also use built in function for this 
list.clear()
list = [zip(*matrix)]
print(list)




