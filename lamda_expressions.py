def make_incrementor(y, n):
    return lambda x: x + y + n
f = make_incrementor(10, 50);
print(f(5))
print(f(12))