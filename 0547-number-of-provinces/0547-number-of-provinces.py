class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n = number of cities
        n = len(isConnected)
        visit = [0]*n
        numberOfComponents=0
            
        def bfs(node, isConnected, visit):
            queue=deque([node])
            visit[node]=1
            while queue:
                city=queue.popleft()
                for i in range(0,n):
                    if isConnected[city][i]==1 and visit[i]==0:
                        queue.append(i)
                        visit[i]=1
            
            
        for i in range(0,n):
            if visit[i]==0:
                numberOfComponents+=1
                bfs(i, isConnected, visit)
                
        return numberOfComponents