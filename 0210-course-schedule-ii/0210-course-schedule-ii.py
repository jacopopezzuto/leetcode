class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={}
        for a,b in prerequisites:
            if a in courses:
                courses[a].append(b)
            else:
                courses[a]=[b]
        print(courses)
        
        result=[]
        cycle=set()
        visited=set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            if course in courses:
                for item in courses[course]:
                    res=dfs(item)
                    if res==False:
                        return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
            
        for course in range(0,numCourses):
            if dfs(course)==False:
                return []
        return result
            