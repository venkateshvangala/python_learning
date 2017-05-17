n = int(input("enter range: "))
for x in range(2, n):
    if x % 2 == 0:
        print(x, " is even number")
else:
    print("printed all event numbers")
