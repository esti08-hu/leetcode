class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for nxt in graph[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
        
        return indegree == [0] * numCourses


