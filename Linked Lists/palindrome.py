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
    
    def number(self,list1):
        res = 0
        while list1:
            res = res * 10 + list1.value
            list1 = list1.next
        return res
    
    def palindrome(self,num):
        num = str(num)
        if len(num) == 1:
            return True
        if len(num) == 2:
            return num[0] == num[1]
        if num[0] == num[-1]:
            return self.palindrome(num[1:-1])
        return False
    
if __name__ == '__main__':
    llist = linkedList(1)
    second = linkedList(2)
    third = linkedList(1)
    llist.next = second
    second.next = third
    llist.printList()
    head = llist.number(llist)
    print(llist.palindrome(head))