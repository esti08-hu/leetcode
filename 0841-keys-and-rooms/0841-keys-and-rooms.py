class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        dq = deque([0])
        visited = set()
        while dq:
            room = dq.popleft()

            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    dq.append(key)

        if len(visited)  == len(rooms):
            return True 
        else:
            return False