class Solution:
    def dfs(self,source,destination,adjList,visited):
        if visited[source]:
            return False
        if source == destination:
            return True
        visited[source] = True
        for vertex in adjList[source]:
            if self.dfs(vertex,destination,adjList,visited):
                return True
        return False
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for i in range(n)]
        adjList = [[] for i in range(n)]
        for node1,node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        return self.dfs(source, destination, adjList, visited)