# Dictionary looping
print("Dictionary looping")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, ' -> ', v)
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# looping throught the sequence inorder to get index position and value at the same time 
# by using enumerate
# Example: 1
sequence = [1, 2, 3, 4, 5, 6]
for position, value in enumerate(sequence):
    print(position, '-->', value)
# Example: 2
for index, value in enumerate(['tic', 'tac', 'toe']):
    print(index, '-->', value)

print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# To loop over two or more sequences at the same time, 
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# To loop over a sequence in reverse, first specify 
# the sequence in a forward direction and then call the reversed()
# Example: 1
list = [x for x in range(1, 10, 2)]
for value in reversed(list):
    print(value)


# Example: 2 with index
list = [x for x in range(1, 10, 2)]
for index, value in enumerate(reversed(list)):
    print(index, '-> ', value)



# Example: 3 
list = [x for x in range(1, 10, 2)]
for index, value in enumerate(range(1, 10, 2)):
    print(index, '-> ', value)

# To loop over a sequence in sorted order, use the sorted() function 
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for x in sorted(set(basket)):
    print(x)
