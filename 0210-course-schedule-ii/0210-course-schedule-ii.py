class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for nb in graph[course]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)

        return order if len(order) == numCourses else []