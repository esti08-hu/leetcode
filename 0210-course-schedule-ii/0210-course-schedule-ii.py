class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            
        q = deque([course for course in range(numCourses) if indegree[course] == 0])
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nb in graph[course]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        return res if len(res) == numCourses else []