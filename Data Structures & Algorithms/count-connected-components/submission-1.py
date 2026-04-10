class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        visited = set()
        graph = defaultdict(list)

        def dfs(i):
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
