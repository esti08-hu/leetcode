class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0
        
        while q:
            course = q.popleft()
            visited+=1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return visited == numCourses
        
