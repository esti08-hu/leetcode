class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses

        for a, b in prerequisites:
            inDegree[a] +=1
        

        graph = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for nb in graph[course]:
                inDegree[nb] -= 1
                if inDegree[nb] == 0:
                    q.append(nb)
        
        return order if len(order)==numCourses else []
