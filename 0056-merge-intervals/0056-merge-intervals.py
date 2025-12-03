class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []

        curr_interval = intervals[0]

        for s, e in intervals[1:]:
            if curr_interval[1] < s:
                res.append(curr_interval)
                curr_interval = [s, e]
            else:
                curr_interval[1] = max(curr_interval[1], e)
        
        res.append(curr_interval)
        return res
