from collections import deque

queue = deque(['Mateo', 'Cristian', 'Sofia'])

queue.append('Kathe')
queue.append('Josue')

print(queue)

queue.popleft()
print(queue)
