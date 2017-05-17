n = int(input("enter range: "))
for x in range(2, n):
    for num in range(2, x):
        if(x % num == 0):
            print(x, " is equals to ", num, " * ", x // num)
            break
    else:
        print(x, " is prime number")