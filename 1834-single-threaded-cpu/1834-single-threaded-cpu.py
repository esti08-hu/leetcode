class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []

        tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
        n = len(tasks)
        res = []
        i = 0
        time = 0

        while i < n or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            while i < n and tasks[i][0] <= time:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1

            if heap:
                duration, idx = heappop(heap)
                res.append(idx)
                time += duration
        
        return res