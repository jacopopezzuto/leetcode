class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        def bfs(i):
            queue=deque([i])
            visited[i]=True
            while queue:
                j=queue.popleft()
                for z,k in enumerate(isConnected[j]):
                    if k==1 and visited[z]==False:
                        queue.append(z)
                        visited[z]=True
        result=0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                result+=1
        return result
            