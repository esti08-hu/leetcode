class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, course in prerequisites:
            adj[pre].append(course)
        q = deque()
        
        for i in range(numCourses):
            q.append(i)
            visited = set()
            
            while q:
                node = q.popleft()
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            adj[i] = visited

        res = []
        for pre, course in queries:
            res.append(course in adj[pre])
        return res
