class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={}
        for (a,b) in prerequisites:
            if a in adj_list:
                adj_list[a].append(b)
            else:
                adj_list[a]=[b]
        print(adj_list)
        
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if course not in adj_list or adj_list[course]==[]:
                return True
            visited.add(course)
            for i in adj_list[course]:
                result=dfs(i)
                if result==False:
                    return False
            visited.remove(course)
            adj_list[course]=[]
            return True
        for course in range(0,numCourses):
            if not dfs(course):
                return False
        return True