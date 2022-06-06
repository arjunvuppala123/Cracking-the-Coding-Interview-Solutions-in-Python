class adjacentMatrix:
	def __init__(self,size):
		self.adjacentMatrix = []
		for i in range(size):
			self.adjacentMatrix.append([0 for _ in range(size)])
		self.size = size
	def insert(self,v1,v2):
		self.adjacentMatrix[v1][v2] = 1
		self.adjacentMatrix[v2][v1] = 1
	def delete(self,v1,v2):
		if self.adjacentMatrix[v1][v2] == 0:
			return
		self.adjacentMatrix[v1][v2] = 0
		self.adjacentMatrix[v2][v1] = 0
	def len(self):
		return self.size
	def printMatrix(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.adjacentMatrix[i][j],end = " ")
			print()

if __name__ == "__main__":
	g = adjacentMatrix(5)
	g.insert(0, 1)
	g.insert(0, 2)
	g.insert(1, 2)
	g.insert(2, 0)
	g.insert(2, 3)
	print("Adjacent Matrix:")
	g.printMatrix()
	g.delete(0, 1)
	g.delete(2,2)
	print("Adjacent Matrix:")
	g.printMatrix()
