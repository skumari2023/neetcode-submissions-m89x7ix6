class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        adj = {i:[] for i in range(numCourses)}

        for c, pre in prerequisites:
            adj[c].append(pre)
        
        def dfs(i):
            #indicates loop and this only works on DAG (directed acyclic graphs)
            if i in visited:
                return False
            if adj[i] == []:
                return True
            
            visited.add(i)
            
            for j in adj[i]:
                if not dfs(j):
                    return False
            
            visited.remove(i)
            adj[i] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True