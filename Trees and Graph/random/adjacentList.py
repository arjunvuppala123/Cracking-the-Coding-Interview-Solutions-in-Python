class Node:
	def __init__(self,value):
		self.vertex = value 
		self.next = None

class adjacentList:
	def __init__(self,size):
		self.vertices = size
		self.graph = [None]*self.vertices
	def insert(self,s,d):
		node = Node(d)
		node.next = self.graph[s]
		self.graph[s] = node  

		node = Node(s)
		node.next = self.graph[d]
		self.graph[d] = node 
	def printList(self):
		for i in range(self.vertices):
			print("Vertex "+str(i)+":",end=" ")
			temp = self.graph[i]
			while temp:
				print("-> {}".format(temp.vertex),end=" ")
				temp = temp.next
			print("\n")

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = adjacentList(V)
    graph.insert(0, 1)
    graph.insert(0, 2)
    graph.insert(0, 3)
    graph.insert(1, 2)

    graph.printList()