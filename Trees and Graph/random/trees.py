class Node:
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

def insert(root,value):
	if root is None:
		return Node(value)
	else:
		if root.value == value:
			return root
		elif root.value > value:
			root.right = insert(root.right,value)
		else:
			root.left = insert(root.left,value)
	return root

def inOrder(root):
	if root:
		inOrder(root.left)
		print(root.value)
		inOrder(root.right)

def preOrder(root):
	if root:
		print(root.value)
		preOrder(root.left)
		preOrder(root.right)

def postOrder(root):
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print(root.value)


def minValueNode(node):
	curr = node 
	while (curr.next):
		curr = curr.next
	return curr

def delete(root,key):
	if root is None:
		return root

	if root.value > key:
		root.left = delete(root.left,key)
	elif root.value < key:
		root.right = delete(root.right,key)
	else:
		if root.left is None:
			temp = root.right 
			root = None
			return temp
		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = minValueNode(root.right)
		root.key = temp.key
		root.right = delete(root.right,temp.key)
	return root

if __name__ == '__main__':
	root = None
	root = insert(root,10)
	root = insert(root,20)
	root = insert(root,30)
	root = insert(root,40)
	root = insert(root,50)
	root = insert(root,25)
	root = insert(root,15)
	print("INORDER")
	inOrder(root)
	print("PREORDER")
	preOrder(root)
	print("POSTORDER")
	postOrder(root)
	root = delete(root,20)
	print("INORDER")
	inOrder(root)
	print("PREORDER")
	preOrder(root)
	print("POSTORDER")
	postOrder(root)
	root = delete(root,10)
	print("INORDER")
	inOrder(root)
	print("PREORDER")
	preOrder(root)
	print("POSTORDER")
	postOrder(root)
