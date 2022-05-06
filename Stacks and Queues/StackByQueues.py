'''
write a program to implement a stack as a queue
'''
from collections import deque

class stackAsQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,value):
        self.queue.append(value)

    def pop(self):
        for i in range(len(self.queue)-1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def printStack(self):
        print(list(self.queue))

    def top(self):
        return self.queue[-1]

if __name__ == '__main__':
    stack = stackAsQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    print("STACK")
    stack.printStack()
    print("TOP: ")
    print(stack.top())
