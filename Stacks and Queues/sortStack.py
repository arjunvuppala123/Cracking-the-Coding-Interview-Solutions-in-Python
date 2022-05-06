class stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        self.stack.sort()

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def printStack(self):
        print("Stack: ")
        print(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
    
if __name__ == '__main__':
    stack = stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.printStack()
    stack.pop()
    stack.printStack()
    print("TOP: ")
    print(stack.peek())