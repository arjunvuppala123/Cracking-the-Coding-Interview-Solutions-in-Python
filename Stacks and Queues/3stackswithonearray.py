'''
write a program to implement 3 stacks with one array
'''

class threeStacks:
    def __init__(self):
        self.stack = []
        self.stack1 = []
        self.stack2 = []

    def push(self,array):
        array1 = array.copy()
        array2 = array.copy()
        array3 = array.copy()
        while len(array1) > 0:
            self.stack.append(array1.pop())
        while len(array2) > 0:
            self.stack1.append(array2.pop())
            self.stack1 = self.stack1[::-1]
        while len(array3) > 0:
            mid = len(array3)//2
            self.stack2.insert(array3.pop(),mid)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop()
        if len(self.stack1) == 0:
            print("Stack is empty")
        else:
            self.stack1.pop()
        if len(self.stack2) == 0:
            print("Stack is empty")
        else:
            self.stack2.pop()
    
    def top(self):
        return [self.stack[-1], self.stack1[-1], self.stack2[-1]]
    
    def printStacks(self):
        print("\n")
        print("Stacks: ")
        print("Stack 1: ", self.stack)
        print("Stack 2: ", self.stack1)
        print("Stack 3: ", self.stack2)
        print("\n")

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    stack = threeStacks()
    stack.push(array)
    stack.printStacks()
    stack.pop()
    stack.pop()
    stack.printStacks()
    
