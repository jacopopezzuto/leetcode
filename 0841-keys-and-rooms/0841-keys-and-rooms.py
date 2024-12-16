class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        visited[0]=True
        stack = [0]
        while stack:
            node = stack.pop()
            for room in rooms[node]:
                if not visited[room]:
                    visited[room]=True
                    stack.append(room)
        for visit in visited:
            if visit==False:
                return False
        return True
                    