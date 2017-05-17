for n in range(10, 100):
    temp, sum = n, 0    
    while n > 0:
        r = n % 10
        sum = (sum * 10) + r
        n = n // 10
    if sum == temp:
        print(temp, " is a palindrom")