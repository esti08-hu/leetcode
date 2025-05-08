class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap  = []
        tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
        n = len(tasks)
        result = []
        i = 0
        time = 0
        while i < n or heap:
            if not heap:
                time = max(time, tasks[i][0])
            while i < n and tasks[i][0] <= time:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            duration, index = heappop(heap)
            result.append(index)
            time += duration
        return result