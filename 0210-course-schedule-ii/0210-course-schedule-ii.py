class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        build the graph and indegree
        enqueue courses indegeree with 0
        process or add the res 
        '''

        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            indegree[a]+=1
            graph[b].append(a)
        
        res = []
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
                q.append(i)
        
        while q:
            for i in range(len(q)):
                course = q.popleft()

                for nei in graph[course]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                        res.append(nei)
        
        return res if len(res) == numCourses else []
        


