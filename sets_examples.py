# A set is an unordered collection with no duplicate elements. Set can created by using set() or {}

# To create a empty set 
emptySet = set() # we should not use {}
print("empty set is: ", emptySet)
print("empty set lenght is: ", len(emptySet))

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} 
# (or) 
# basket = set[{'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}]

print("set is: ", basket)
print("set length: ", len(basket))

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# To test element in set 
print('Is apple exists in set? ', 'apple' in basket)
print('Is hello exists in set? ', 'hello' in basket)

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

print("unique elements in set: ", a)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# letters in a but not in b
print("letters in a but not in b: ", a - b)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# letters in either a or b
print("letters in either a or b: ", a | b)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# letters in both a and b
print("letters in both a and b: ", a & b)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# letters in a or b but not both
print("letters in a or b but not both: ", a ^ b)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# List Comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print()



