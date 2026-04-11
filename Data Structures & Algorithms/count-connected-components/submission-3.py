class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        visited = set()
        connect = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                connect += 1
        return connect