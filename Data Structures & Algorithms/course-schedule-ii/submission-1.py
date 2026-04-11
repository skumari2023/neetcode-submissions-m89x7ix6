class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        cycle = set()
        output = []
        adj = {i:[] for i in range(numCourses)}

        for c,pre in prerequisites:
            adj[c].append(pre)
        
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            
            cycle.add(i)
            
            for j in adj[i]:
                if not dfs(j):
                    return False
            
            cycle.remove(i)
            visited.add(i)
            adj[i] = []
            output.append(i)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output