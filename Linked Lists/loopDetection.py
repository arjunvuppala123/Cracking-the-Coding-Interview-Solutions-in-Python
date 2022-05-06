'''
write a program to detect loop in linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def detectLoop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop detected")
                return
        print("No loop detected")

if __name__=='__main__':
    llist = linkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    eighth = Node(8)
    ninth = Node(9)
    tenth = Node(10)
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eighth
    eighth.next = ninth
    ninth.next = tenth
    tenth.next = third
    llist.printList()
    llist.detectLoop()
