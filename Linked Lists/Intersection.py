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
    
    def tailsandsize(self):
        temp = self
        length = 1
        while temp.next:
            length += 1
            temp = temp.next
        return temp, length
    
    def intersection(self,l1,l2):
        temp1, size1 = l1.tailsandsize()
        temp2, size2 = l2.tailsandsize()
        if temp1 != temp2:
            return None
        if size1 > size2:
            for i in range(size1 - size2):
                l1 = l1.next
        else:
            for i in range(size2 - size1):
                l2 =l2.next
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1

if __name__ == '__main__':
    llist1 = linkedList(1)
    second1 = linkedList(2)
    third1 = linkedList(3)
    fourth1 = linkedList(4)
    fifth1 = linkedList(5)
    sixth1 = linkedList(6)
    seventh1 = linkedList(7)
    eighth1 = linkedList(8)
    ninth1 = linkedList(9)
    tenth1 = linkedList(10)
    llist1.next = second1
    second1.next = third1
    third1.next = fourth1
    fourth1.next = fifth1
    fifth1.next = sixth1
    sixth1.next = seventh1
    seventh1.next = eighth1
    eighth1.next = ninth1
    ninth1.next = tenth1
    print("first linked list")
    llist1.printList()
    llist2 = linkedList(11)
    second2 = linkedList(12)
    third2 = linkedList(13)
    fourth2 = linkedList(14)
    llist2.next = second2
    second2.next = third2
    third2.next = fourth2
    fourth2.next = fifth1
    print("second linked list")
    llist2.printList()
    head = llist1.intersection(llist1,llist2)
    print(head.value)