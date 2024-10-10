class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        status = [False]*len(rooms)
        status[0] = True
        while queue:
            for i in range(0,len(queue)):
                node = queue.popleft()
                for nei in rooms[node]:
                    if status[nei] == False:
                        status[nei]=True
                        queue.append(nei)
        for i in range(0,len(status)):
            if status[i] == False:
                return False
        return True