# List Methods with examples 
a = [1, 2, 3, 4, 5, 6]
print(a)

# append(ele)
a.append(7)
print("list after append: ", a)
print('------------------------------------------')
# extend(list)
a.extend([8, 9, 10])
print("list after extend: ", a)
print('------------------------------------------')
# insert(pos, ele)
a.insert(0, 0)
print("list after insert: ", a)
print('------------------------------------------')
# remove(ele) -- removes the first elem in the list returns error if elem is not present
a.remove(10)
print("list after remove elem: ", a)
print('------------------------------------------')
# pop(position/index) -- remove and returns the element at given posiotion and if position is not found returns last element
a.pop(0)
print("list after pop: ", a)
print('------------------------------------------')
# clear() == del list[:] -- remove all elements in the list
a.clear()
print("list after clear: ", a)
print('------------------------------------------')
# index(elem, [start, end]) -- returns zero based index of elem in list. Raises a ValueError if there is no such item. 
a = [1, 2, 3, 4, 5, 6, 7]
print("index of 3: ", a.index(3))
print("index of 5 from list 1 to 4", a.index(5, 1, 5))
print('------------------------------------------')
# count(elem) -- returns number of times that elem occurs
a = [1, 2, 3, 4, 1, 1, 3, 2]
print("no of occurances of 1: ", a.count(1))
print('------------------------------------------')
# reverse() -- reverse the list elements in place
print("list after reverse: ", a.reverse())
print('------------------------------------------')
# copy() -- returns the shallow copy of the list Equivalent to a[:].
a = [1, 2, 3, 4, 5, 6]
b = a.copy()
b.append(8)
print("list a elements: ", a)
print("list b elements(shallow copy): ", b)
print('------------------------------------------')
# sort(key = None, reverse = False) -- Sort the items of the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a.sort(key = None, reverse = True)
print("after sort list elements: ", a)
a.sort()
print("after sort list elements: ", a)
print('------------------------------------------')

