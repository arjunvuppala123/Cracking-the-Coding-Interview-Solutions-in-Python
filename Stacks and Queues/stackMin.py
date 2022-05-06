from sys import maxsize

class stackMin:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self,stack):
        return len(stack) == 0
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self,value):
        if (self.isEmpty(self.stack)):
            return str(-maxsize -1) 
     
        return self.stack.pop()

    def min(self):
        sorted_stack = sorted(self.stack)
        return sorted_stack[0]
    
    def printStack(self):
        print(self.stack)
    
    def top(self):
        print("Top element is:" + str(self.stack[-1]))

if __name__ == '__main__':
    stack = stackMin()
    stack.push(3)
    stack.top()
    stack.push(5)
    stack.top()
    stack.push(2)
    stack.push(-1)
    stack.pop(4)
    print("Stack:",stack.stack)
    print("Min:",stack.min())
