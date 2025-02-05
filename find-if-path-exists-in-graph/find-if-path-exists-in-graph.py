class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list={}
        for edge in edges:
            x,y=edge
            if x not in adj_list:
                adj_list[x]=[]
            adj_list[x].append(y)
            if y not in adj_list:
                adj_list[y]=[]
            adj_list[y].append(x)
        visited=set()
        def dfs(node):
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for item in adj_list[node]:
                    if dfs(item):
                        return True
            return False
                
        return dfs(source)
        