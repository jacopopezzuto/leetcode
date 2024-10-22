class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={}
        for x,y in prerequisites:
            if x in courses:
                courses[x].append(y)
            else:
                courses[x]=[y]
        result=[]
        visited=set()
        cycle=set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            if course in courses:
                for c in courses[course]:
                    res=dfs(c)
                    if res==False:
                        return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
        
        for i in range(0,numCourses):
            if dfs(i)==False:
                return []
        return result