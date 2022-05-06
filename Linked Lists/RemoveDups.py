import time

class Node:

	def __init__(self, data):

		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None

	def printlist(self):

		temp = self.head

		while (temp):
			print(temp.data, end=" ")
			temp = temp.next

	def removeDuplicates(self, head):
		if self.head is None or self.head.next is None:
			return head

		hash = set()

		current = head
		hash.add(self.head.data)

		while current.next is not None:

			if current.next.data in hash:
				current.next = current.next.next
			else:
				hash.add(current.next.data)
				current = current.next

		return head


if __name__ == "__main__":
	llist = LinkedList()
	llist.head = Node(10)
	second = Node(12)
	third = Node(11)
	fourth = Node(11)
	fifth = Node(12)
	sixth = Node(11)
	seventh = Node(10)

	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = fifth
	fifth.next = sixth
	sixth.next = seventh

	print("Linked List before removing Duplicates.")
	llist.printlist()
	start_time = time.time()
	llist.removeDuplicates(llist.head)
	print("\nLinked List after removing duplicates.")
	llist.printlist()
	print("\nTime taken: %s seconds" % (time.time() - start_time))
