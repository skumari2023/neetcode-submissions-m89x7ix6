class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #empty graph = tree
        if n == 0:
            return True
        
        visited = set()
        adj = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        #have prev val for undirected graphs
        def dfs(i, prev):
            if i in visited:
                return False
        
            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visited)
