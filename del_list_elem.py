a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print("after delete specified position element:")
print(a)

print("after delete specified positions with start and end positions:")
del a[2:4]
print(a)

print("delete entire list elements")
del a[:]
print(a)
