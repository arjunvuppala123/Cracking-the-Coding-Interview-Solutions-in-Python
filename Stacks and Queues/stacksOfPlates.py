class setOfStacks:
    def __init__(self, max_size=0):
        self.stacks = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.max_size:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        if len(self.stacks[-1]) == 1:
            self.stacks.pop()
        else:
            self.stacks[-1].pop()

    def popAt(self, index):
        if len(self.stacks) == 0:
            return None
        if len(self.stacks[index]) == 1:
            self.stacks.pop(index)
        else:
            self.stacks[index].pop()
            
    def print(self):
        print("Stacks")
        for i in range(len(self.stacks)):
            print("Stack ", i+1, ": ", end="")
            print(self.stacks[i])

if __name__ == '__main__':
    s = setOfStacks(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    s.push(16)
    s.print()
    s.pop()
    s.print()
    s.popAt(0)
    s.popAt(2)
    s.print()
