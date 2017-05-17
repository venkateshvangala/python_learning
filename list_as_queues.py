from collections import deque
queue = deque([1, 2, 3, 4, 5, 6])
queue.append(7)
queue.append(8)

print("queue after insert: ", queue)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("poped element: ", queue.popleft())
print("queue after pop: ", queue)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("poped element: ", queue.popleft())
print("queue after pop: ", queue)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("queue elements are: ", queue)
