class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n = number of cities
        n = len(isConnected)
        visit = [0]*n
        numberOfComponents=0
        
        def dfs(node,isConnected,visit):
            visit[node]=1
            for i in range(0,n):
                if isConnected[node][i]==1 and visit[i]==0:
                    dfs(i,isConnected,visit)
            
            
        for i in range(0,n):
            if visit[i]==0:
                dfs(i,isConnected,visit)
                numberOfComponents+=1
        return numberOfComponents