# looping through dictionaries, the key and corresponding value 
# can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, '->', value)
