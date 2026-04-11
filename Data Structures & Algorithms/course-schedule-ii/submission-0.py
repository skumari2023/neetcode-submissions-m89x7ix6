class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        cycle = set()
        output = []
        adj = {i:[] for i in range(numCourses)}

        for c, pre in prerequisites:
            adj[c].append(pre)
        
        def dfs(i):
            #cycle detects loop
            if i in cycle:
                return False
            #lets us know that this course and all its prereqs are already verified 
            #so don't need to check again
            if i in visited:
                return True
            
            cycle.add(i)
            
            for j in adj[i]:
                if not dfs(j):
                    return False
            
            cycle.remove(i)
            visited.add(i)
            output.append(i)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output 

            