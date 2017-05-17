def fabinacci(range):
    # function with return value 
    a, b = 0, 1
    result = [];
    while a < range:
        result.append(a)
        a, b = b, a+b
    else: 
        print("Fabinacci numbers upto ", range)
    return result

numbers = fabinacci(100)
print(numbers)