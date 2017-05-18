# It is best to think of a dictionary as an unordered set of key: value pairs, 
# with the requirement that the keys are unique (within one dictionary). 
# A pair of braces creates an empty dictionary: {}.

# Create empty dictionary
emptyDic = {}
print("empty dictionary is: ", emptyDic)
print("empty dictionary length: ", len(emptyDic))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# Step:1 to create a dictionay
tel = {'jack': 4098, 'sape': 4139}
print("dictionary elements are: ", tel)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# Step:2 to create dictionary 
tel.clear()
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("dictionary elements are: ", tel)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# Step:3 to create dictionary
tel.clear()
tel = dict(sape=4139, guido=4127, jack=4098)
print("dictionary elements are: ", tel)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()


# Adding elements to dictionary
tel['irv'] = 4127
print("after adding, dictionary elements are: ", tel)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# retrieving dictionary element 
print("retrieve element from dic is: ", tel['sape'])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# Delete element from dictionary
del tel['sape']
print("dictionary after delte element is: ", tel)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# display all keys in dictionary 
keys = list(tel.keys())
print("all keys in dict are: ", keys)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# display all keys in sorted order are 
keys = sorted(tel.keys())
print("all keys in dict are: ", keys)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

# comprehension produce dictionary 
dict = {x: x**2 for x in [1, 2, 3, 4]}
print("dictionary elements are: ", dict)
print()