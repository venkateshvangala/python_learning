def fabinacci(range):
    '''Print all the fabinacci numbers upto ${range}'''
    a, b = 0, 1;
    while b < range:
        print(b, end=' ')
        a, b = b, a + b;
    else: print()

fabinacci(100)