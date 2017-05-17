n = int(input("enter range: "))
for x in range(2, n):
    if x % 2 == 0:
        print(x, " is even")
        continue
    print(x, " is odd")
else:
    print("printed all even and odd number upto ", n)