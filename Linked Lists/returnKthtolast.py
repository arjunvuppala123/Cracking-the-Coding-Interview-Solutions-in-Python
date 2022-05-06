class linkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def printList(self):
        temp = self
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
    
    def returnKthToLast(self, k):
        temp = self
        length = 0
        while temp:
            temp = temp.next
        if length < k:
            return None
        temp = self
        for i in range(length - k):
            temp = temp.next
        return temp
    
if __name__ == '__main__':
    llist = linkedList(1)
    second = linkedList(2)
    third = linkedList(3)
    fourth = linkedList(4)
    fifth = linkedList(5)
    sixth = linkedList(6)
    seventh = linkedList(7)
    eighth = linkedList(8)
    ninth = linkedList(9)
    tenth = linkedList(10)
    llist.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eighth
    eighth.next = ninth
    ninth.next = tenth
    llist.printList()
    head = llist.returnKthToLast(3)
    head.printList()