#Python stack created by list
pythonStack = []

#Appends elements to the top of a stack
pythonStack.append('a')
pythonStack.append('b')
pythonStack.append('c')
print(pythonStack)

#Removes the last item in the list/newest item in a stack (LIFO)
pythonStack.pop()
print(pythonStack)

#Issues with a list are memory issues as it grows

#Using deque creates and actual stack that is faster as it is a doubly linked list. Faster for adding at the end/removing the end, but slower for parsing through the structure for a specific item
from collections import deque
dequeStack = deque()

dequeStack.append('c')
dequeStack.append('b')
dequeStack.append('a')
print(dequeStack)

dequeStack.pop()
print(dequeStack)
