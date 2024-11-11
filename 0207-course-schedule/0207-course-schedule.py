class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={}
        for x,y in prerequisites:
            if x in adj:
                adj[x].append(y)
            else:
                adj[x]=[y]
        visited=set()
        def dfs(i):
            if i not in adj or len(adj[i])==0:
                return True
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if dfs(j)==False:
                    return False
            visited.remove(i)
            adj[i]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        