x = int(input("please enter a number:"))
if x == 0:
    print("Zero")
elif x < 0:
    x = 0
    print("negative changed to zero")
elif x == 1:
    print("Single")
else:
    print("More")